import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtCore import QDate
from modelo.empresa import Empresa
from modelo.datos import ManejarJson
from modelo.arquitecto import Arquitecto
from modelo.cliente import Cliente
from modelo.proyecto_vial import ProyectoVial
from modelo.proyecto_edificacion import ProyectoEdificacion
from modelo.direccion import Direccion
from vista.ventana_principal import VentanaPrincipal
from vista.menu import Menu
from vista.lista import Tabla
from vista.agregar_arquitecto import VistaArquitecto
from vista.agregar_cliente import VistaCliente
from vista.agregar_proyecto import VistaProyecto
from vista.acerca_de import AcercaDe
from modelo.llenar_tabla import LLenarTabla
from modelo.lista_arquitectos_clientes import LlenarLista
from controlador.controlador_presupuesto import ControladorPresupuesto
from controlador.controlador_por_ciento import PorCiento
from controlador.controlador_cliente import DatosCliente
from controlador.controlador_cumplimiento import ModificarCumplimiento
from controlador.controlador_promedio import CalcularPromedio

class ControladorPrincipal:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = QtWidgets.QStackedWidget()
        self.widget.setMinimumHeight(800)
        self.widget.setMinimumWidth(880)
        
        
        self.empresa = Empresa()
        self.json = ManejarJson()
        self.arquitecto = {}
        self.cliente = {}
        
        
        self.datos_arquitecto = VistaArquitecto()
        self.datos_cliente = VistaCliente()
        self.datos_proyecto = VistaProyecto()
        self.listar_arquitectos_clientes = LlenarLista(self.datos_proyecto)
        self.controlador_presupuesto = ControladorPresupuesto()
        self.controlador_por_ciento = PorCiento()
        self.controlador_cliente = DatosCliente()
        self.controlador_cumplimiento = ModificarCumplimiento()
        self.controlador_promedio = CalcularPromedio()
        self.tabla = Tabla(self)
        self.menu = Menu(self)
        self.acercade = AcercaDe()
        self.widget_principal = self.menu.stackedWidget
        
        self.widget_principal.addWidget(self.tabla)
        self.widget_principal.addWidget(self.controlador_cliente.v_cliente)
        self.widget_principal.addWidget(self.controlador_cumplimiento.v_cumplimiento)
        self.widget_principal.addWidget(self.controlador_por_ciento.v_por_ciento)
        self.widget_principal.addWidget(self.controlador_presupuesto.v_presupuesto)
        self.widget_principal.addWidget(self.controlador_promedio.promedio_v)
        self.widget_principal.addWidget(self.acercade)

        self.ultimo_id_arqui = 0
        self.ultimo_id_cliente = 0
        self.determinar_ids()

        
    def iniciar(self):
        self.vista1 = VentanaPrincipal(self)
        self.widget.addWidget(self.vista1)
        self.widget.addWidget(self.menu) 
        self.widget.show()
        self.widget.resize(1536, 864)
        centro = QDesktopWidget().availableGeometry().center()
        ventana = self.widget.frameGeometry()
        ventana.moveCenter(centro)
        self.widget.move(ventana.topLeft())
        
        self.app.exec_()

    def ir_atras(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def iniciar_menu(self):
        self.widget.setCurrentWidget(self.menu)
        self.menu.menu_desplegable.setVisible(True)
        self.menu.widget_2.setHidden(True)
        self.menu.pushButton.setChecked(True)
        self.iniciar_lista()

    def iniciar_lista(self):
        self.widget_principal.setCurrentWidget(self.tabla)
        self.llenar_tabla = LLenarTabla(self.tabla)
        self.llenar_tabla.tabla()
    
    def determinar_ids(self):
        self.dicc = self.json.cargar_datos()
        for a in self.dicc["Arquitectos"]:
            if a["id_"] > self.ultimo_id_arqui:
                self.ultimo_id_arqui = a["id_"]
        for b in self.dicc["Clientes"]:
            if b["id_"] > self.ultimo_id_cliente:
                self.ultimo_id_cliente = b["id_"]

    def agregar(self):
        self.accion = self.tabla.sender().text() 
        if self.accion == "Arquitecto":
            if self.datos_arquitecto.exec_():
                self.ultimo_id_arqui += 1
                id_ = self.ultimo_id_arqui
                nombre = self.datos_arquitecto.nombre
                sexo = self.datos_arquitecto.sexo
                exp = self.datos_arquitecto.exp
                self.arquitecto = Arquitecto(id_, nombre, sexo, exp)
                self.arquitecto = self.arquitecto.diccio()
                self.agregar_arquitect()
        elif self.accion == "Cliente":
            if self.datos_cliente.exec_():
                self.ultimo_id_cliente += 1
                id_ = self.ultimo_id_cliente
                nombre = self.datos_cliente.nombre
                sexo = self.datos_cliente.sexo
                direccion = Direccion(self.datos_cliente.calle, self.datos_cliente.numero, self.datos_cliente.municipio, self.datos_cliente.provincia)
                direccion = direccion.diccio()
                tipo_entidad = self.datos_cliente.tipo_entidad
                self.cliente = Cliente(id_, nombre, sexo, direccion, tipo_entidad)
                self.cliente = self.cliente.diccio()
                
                self.agregar_client()
        elif self.accion == "Proyecto":
            self.proximo_ci = self.dicc["Proximo codigo"]
            if self.dicc["Proyectos"]:
                for i in range(len(self.dicc["Proyectos"])):
                    if self.proximo_ci <= self.dicc["Proyectos"][i]["codigo_identificacion"]:
                        self.proximo_ci = self.dicc["Proyectos"][i]["codigo_identificacion"] +1
            
            if len(self.empresa.dicc["Arquitectos"]) == 0 or len(self.empresa.dicc["Clientes"]) == 0:
                QMessageBox.warning(self.tabla, "Aviso", "Para agregar un nuevo proyecto debe tener al menos un arquitecto y un cliente")
            else:
                self.listar_arquitectos_clientes.lista()
                codigo_identificacion = self.proximo_ci
                self.datos_proyecto.codigo_.setText(str(codigo_identificacion))
                if self.datos_proyecto.exec_():
                    
                    tipo = self.datos_proyecto.tipo
                    nombre = self.datos_proyecto.nombre
                    cliente= self.datos_proyecto.client
                    
                    presupuesto = self.datos_proyecto.presupuesto
                    
                    fecha_inicio = self.datos_proyecto.fecha_inicio
                    duracion = self.datos_proyecto.duracion
                    arquitecto = self.datos_proyecto.arquitect
                    cumplimiento = self.datos_proyecto.cumplimiento
                    tipo_especifico = self.datos_proyecto.tipo_especifico

                    if tipo == "edificacion":
                        altura = self.datos_proyecto.altura
                        direccion = Direccion(self.datos_proyecto.calle, self.datos_proyecto.numero, self.datos_proyecto.municipio, self.datos_proyecto.provincia)
                        direccion = direccion.diccio()
                        self.proyecto_edificacion = ProyectoEdificacion(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, altura, direccion)
                        self.proyecto_edificacion = self.proyecto_edificacion.diccio()
                        self.agregar_proyecto_edificacion()
                        self.verificar_uso()
                    else:
                        longitud = self.datos_proyecto.longitud
                        dentro_de_provincia = self.datos_proyecto.dentro_de_provincia
                        self.proyecto_vial = ProyectoVial(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, longitud, dentro_de_provincia)
                        self.proyecto_vial = self.proyecto_vial.diccio()
                        self.agregar_proyecto_vial()
            
        self.tabla.todos.setChecked(True)
        self.verificar_uso() 


    def agregar_arquitect(self):
        self.empresa.agregar_arquitecto(self.arquitecto)
        self.llenar_tabla.tabla()

    def agregar_client(self):
        self.empresa.agregar_cliente(self.cliente)
        self.llenar_tabla.tabla()

    def agregar_proyecto_edificacion(self):
        self.empresa.agregar_proyecto(self.proyecto_edificacion, self.proximo_ci+1)
        self.llenar_tabla.tabla()

    def agregar_proyecto_vial(self):
        self.empresa.agregar_proyecto(self.proyecto_vial, self.proximo_ci+1)
        self.llenar_tabla.tabla()

    def eliminar(self):
        self.dicc = self.json.cargar_datos()
        self.verificar_uso()
        if self.tabla.tWarquitecto.selectedItems():
            fila = self.tabla.tWarquitecto.currentRow()
            if self.dicc["Arquitectos"][fila]["en_uso"]:
                QMessageBox.warning(self.tabla, "Error", "No puede eliminar ningún arquitecto que esté asociado a algún proyecto")
            else:
                self.tabla.tWarquitecto.removeRow(fila)
                self.empresa.eliminar_elm("Arquitectos", fila)
        if self.tabla.tWcliente.selectedItems():
            fila = self.tabla.tWcliente.currentRow()
            if self.dicc["Clientes"][fila]["en_uso"]:
                QMessageBox.warning(self.tabla, "Error", "No puede eliminar ningún cliente que esté asociado a algún proyecto")
            else:
                self.tabla.tWcliente.removeRow(fila)
                self.empresa.eliminar_elm("Clientes", fila)
        if self.tabla.tWproyecto.selectedItems():
            fila = self.tabla.tWproyecto.currentRow()
            codigo = self.tabla.tWproyecto.item(fila, 0).text()
            for f in range(len(self.dicc["Proyectos"])):
                if self.dicc["Proyectos"][f]["codigo_identificacion"] == int(codigo):
                    fila = f
                    break
            self.tabla.todos.setChecked(True)
            self.tabla.tWproyecto.removeRow(fila)
            self.empresa.eliminar_elm("Proyectos", fila)


    def modificar(self):
        self.dicc = self.json.cargar_datos()
        if self.tabla.tWarquitecto.selectedItems():
            fila = self.tabla.tWarquitecto.currentRow()
            id_ = self.dicc["Arquitectos"][fila]["id_"]
            nombre = self.tabla.tWarquitecto.item(fila, 0).text()
            sexo = self.tabla.tWarquitecto.item(fila, 1).text()
            exp = self.tabla.tWarquitecto.item(fila, 2).text()
            self.datos_arquitecto.lineEdit.setText(nombre)
            self.datos_arquitecto.spinBox.setValue(int(exp))
            if sexo == "masculino":
                self.datos_arquitecto.masculino.setChecked(True)
            else:
                self.datos_arquitecto.femenino.setChecked(True)
            self.arquitecto = Arquitecto(id_, nombre, sexo, exp)
            self.arquitecto = self.arquitecto.diccio()
            proyectos_con_ese_arquitecto = [p for p in range(len(self.dicc["Proyectos"])) if self.dicc["Proyectos"][p]["arquitecto"]["id_"] == id_]

            if self.datos_arquitecto.exec_():
                
                nombre = self.datos_arquitecto.nombre
                sexo = self.datos_arquitecto.sexo
                exp = self.datos_arquitecto.exp
                self.arquitecto = Arquitecto(id_, nombre, sexo, exp)
                self.arquitecto = self.arquitecto.diccio()
                self.empresa.modificar_elm("Arquitectos", fila, self.arquitecto)
                if proyectos_con_ese_arquitecto:
                    for p in proyectos_con_ese_arquitecto:
                        self.arquitecto["en_uso"] = True
                        proy_a_actualizar = self.dicc["Proyectos"][p]
                        proy_a_actualizar["arquitecto"] = self.arquitecto
                        self.empresa.modificar_elm("Proyectos", p, proy_a_actualizar)
                self.llenar_tabla.tabla()


        if self.tabla.tWcliente.selectedItems():
            fila = self.tabla.tWcliente.currentRow()
            id_ = self.dicc["Clientes"][fila]["id_"]
            nombre = self.tabla.tWcliente.item(fila, 0).text()
            sexo = self.tabla.tWcliente.item(fila, 1).text()
            direccion = self.tabla.tWcliente.item(fila, 2).text()
            lista_dir = direccion.split(",")
            calle = lista_dir[0]
            num = lista_dir[1].lstrip()
            num = int(num[1:])
            municipio = lista_dir[2].lstrip()
            provincia = lista_dir[3].lstrip()
            tipo_entidad = self.tabla.tWcliente.item(fila, 3).text()
            self.datos_cliente.lineEdit_cliente.setText(nombre)
            self.datos_cliente.calle_cliente.setText(calle)
            self.datos_cliente.num_cliente.setValue(num)
            self.datos_cliente.municipio_cliente.setText(municipio)
            self.datos_cliente.prov_cliente.setText(provincia)
            if sexo == "masculino":
                self.datos_cliente.masculino_cliente.setChecked(True)
            else:
                self.datos_cliente.femenino_cliente.setChecked(True)
            if tipo_entidad == "privada":
                self.datos_cliente.privada.setChecked(True)
            else:
                self.datos_cliente.estatal.setChecked(True)

            self.cliente = Cliente(id_, nombre, sexo, direccion, tipo_entidad)
            self.cliente = self.cliente.diccio()
            proyectos_con_ese_cliente = [p for p in range(len(self.dicc["Proyectos"])) if self.dicc["Proyectos"][p]["cliente"]["id_"] == id_]

            if self.datos_cliente.exec_():
                nombre = self.datos_cliente.nombre
                sexo = self.datos_cliente.sexo
                direccion = Direccion(self.datos_cliente.calle, self.datos_cliente.numero, self.datos_cliente.municipio, self.datos_cliente.provincia)
                direccion = direccion.diccio()
                tipo_entidad = self.datos_cliente.tipo_entidad
                self.cliente = Cliente(id_, nombre, sexo, direccion, tipo_entidad)
                self.cliente = self.cliente.diccio()
                self.empresa.modificar_elm("Clientes", fila, self.cliente)
                if proyectos_con_ese_cliente:
                    for p in proyectos_con_ese_cliente:
                        self.cliente["en_uso"] = True
                        proy_a_actualizar = self.dicc["Proyectos"][p]
                        proy_a_actualizar["cliente"] = self.cliente
                        self.empresa.modificar_elm("Proyectos", p, proy_a_actualizar)
                self.llenar_tabla.tabla()

        if self.tabla.tWproyecto.selectedItems():
            fila = self.tabla.tWproyecto.currentRow()
            codigo = self.tabla.tWproyecto.item(fila, 0).text()
            nombre = self.tabla.tWproyecto.item(fila, 1).text()
            tipo = self.tabla.tWproyecto.item(fila, 2).text()
            cliente = self.tabla.tWproyecto.item(fila, 3).text()
            presupuesto = self.tabla.tWproyecto.item(fila, 4).text()
            fecha_inicio = self.tabla.tWproyecto.item(fila, 5).text()
            duracion = self.tabla.tWproyecto.item(fila, 6).text()
            arquitecto = self.tabla.tWproyecto.item(fila, 7).text()
            cumplimiento = self.tabla.tWproyecto.item(fila, 8).text()
            tipo_especifico = self.tabla.tWproyecto.item(fila, 9).text()
            longitud = self.tabla.tWproyecto.item(fila, 10).text()
            dentro_de_provincia = self.tabla.tWproyecto.item(fila, 11).text()
            altura = self.tabla.tWproyecto.item(fila, 12).text()
            direccion = self.tabla.tWproyecto.item(fila, 13).text()
            if direccion != "-":
                direccion = direccion.split(",")
                calle = direccion[0]
                num = direccion[1].lstrip()
                num = int(num[1:])
                municipio = direccion[2].lstrip()
                prov = direccion[3].lstrip()

            self.listar_arquitectos_clientes.lista()
            for c in self.listar_arquitectos_clientes.l_cliente:
                 listac = c.split(" - ")
                 if listac[1] == cliente:
                     self.datos_proyecto.list_clientes.setCurrentRow(int(listac[0]) - 1)
                     break
            for a in self.listar_arquitectos_clientes.l_arqui:
                 listaa = a.split(" - ")
                 if listaa[1] == arquitecto:
                     self.datos_proyecto.list_arquitectos.setCurrentRow(int(listaa[0]) - 1)
                     break

            self.datos_proyecto.nombre_proyecto.setText(nombre)
            self.datos_proyecto.codigo_.setText(codigo)
            self.datos_proyecto.presupuest.setValue(float(presupuesto))
            self.datos_proyecto.cumplimient.setValue(int(cumplimiento))
            self.datos_proyecto.duracio.setValue(int(duracion))
            self.datos_proyecto.fecha_de_inicio.setDate(QDate.fromString(fecha_inicio, "dd-MM-yyyy"))
            
            if tipo == "edificacion":
                self.datos_proyecto.tipo_edificacion.setChecked(True)
                self.datos_proyecto.longitud_o_altura.setValue(int(altura))
                self.datos_proyecto.calle_proyecto.setText(calle)
                self.datos_proyecto.num_proyecto.setValue(num)
                self.datos_proyecto.municipio_proyecto.setText(municipio)
                self.datos_proyecto.prov_proyecto.setText(prov)
            else:
                self.datos_proyecto.tipo_vial.setChecked(True)
                self.datos_proyecto.longitud_o_altura.setValue(int(longitud))
                if dentro_de_provincia == "Si":
                    self.datos_proyecto.checkBox.setChecked(True)

            if tipo_especifico == "industrial" or tipo_especifico == "carretera":
                self.datos_proyecto.tipo_1.setChecked(True)
            elif tipo_especifico == "oficinas" or tipo_especifico == "vias ferreas":
                self.datos_proyecto.tipo_2.setChecked(True)
            else:
                self.datos_proyecto.tipo_3.setChecked(True)

            
            if self.datos_proyecto.exec_():
                tipo = self.datos_proyecto.tipo
                nombre = self.datos_proyecto.nombre
                cliente= self.datos_proyecto.client
                presupuesto = self.datos_proyecto.presupuesto
                codigo_identificacion = int(codigo)
                fecha_inicio = self.datos_proyecto.fecha_inicio
                duracion = self.datos_proyecto.duracion
                arquitecto = self.datos_proyecto.arquitect
                cumplimiento = self.datos_proyecto.cumplimiento
                tipo_especifico = self.datos_proyecto.tipo_especifico

                for f in range(len(self.dicc["Proyectos"])):
                    if self.dicc["Proyectos"][f]["codigo_identificacion"] == int(codigo):
                        fila = f
                        break
                

                if tipo == "edificacion":
                    altura = self.datos_proyecto.altura
                    direccion = Direccion(self.datos_proyecto.calle, self.datos_proyecto.numero, self.datos_proyecto.municipio, self.datos_proyecto.provincia)
                    direccion= direccion.diccio()
                    self.proyecto_edificacion = ProyectoEdificacion(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, altura, direccion)
                    self.proyecto_edificacion = self.proyecto_edificacion.diccio()
                    self.empresa.modificar_elm("Proyectos", fila, self.proyecto_edificacion)
                else:
                    longitud = self.datos_proyecto.longitud
                    dentro_de_provincia = self.datos_proyecto.dentro_de_provincia
                    self.proyecto_vial = ProyectoVial(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, longitud, dentro_de_provincia)
                    self.proyecto_vial = self.proyecto_vial.diccio()
                    self.empresa.modificar_elm("Proyectos", fila, self.proyecto_vial)

                self.llenar_tabla.tabla()
        self.tabla.todos.setChecked(True)
        self.verificar_uso()

    def obtener_proyectos_filtrados(self):
        self.dicc = self.json.cargar_datos()
        proyectos_en_desarrollo = [i for i in self.dicc["Proyectos"] if i["cumplimiento"] < 100]
        proyectos_filtrados = []
        if self.tabla.todos.isChecked():
            proyectos_filtrados = proyectos_en_desarrollo
        else:
            if self.tabla.edificacion.isChecked():
                tipo = "edificacion"
            if self.tabla.vial.isChecked():
                tipo = "vial"
            for d in proyectos_en_desarrollo:
                if d["tipo"] == tipo:
                    proyectos_filtrados.append(d)
        return proyectos_filtrados
    
    def filtrar_proyecto(self):
        proyectos_filtrados = self.obtener_proyectos_filtrados()
        self.llenar_tabla.tabla(proyectos_filtrados) 

    def verificar_uso(self):
        self.dicc = self.json.cargar_datos()
        for a in self.dicc["Arquitectos"]:
            a["en_uso"] = False
        for b in self.dicc["Clientes"]:
            b["en_uso"] = False
        for p in self.dicc["Proyectos"]:
            id_arqui = p["arquitecto"]["id_"]
            id_cliente = p["cliente"]["id_"]
            for a in self.dicc["Arquitectos"]:
                if a["id_"] == id_arqui:
                    a["en_uso"] = True
            for c in self.dicc["Clientes"]:
                if c["id_"] == id_cliente:
                    c["en_uso"] = True
        self.json.guardar_datos(self.dicc)

    def presupuesto(self):
        self.controlador_presupuesto.ordenar_tabla_presupuesto()
        self.widget_principal.setCurrentWidget(self.controlador_presupuesto.v_presupuesto)
        
    def por_ciento(self):
        self.widget_principal.setCurrentWidget(self.controlador_por_ciento.v_por_ciento)
        self.controlador_por_ciento.limpiar()

    def datos_del_cliente(self):
        self.widget_principal.setCurrentWidget(self.controlador_cliente.v_cliente)
        self.controlador_cliente.mostrar_comboBox()
        self.controlador_cliente.limpiar()
            
    def cumplimiento(self):
        self.widget_principal.setCurrentWidget(self.controlador_cumplimiento.v_cumplimiento)
        self.controlador_cumplimiento.mostrar_comboBox()
        self.controlador_cumplimiento.limpiar()

    def promedio(self):
        self.controlador_promedio.calcular_promedio()
        self.widget_principal.setCurrentWidget(self.controlador_promedio.promedio_v)

    def acerca_de(self):
        self.widget_principal.setCurrentWidget(self.acercade)
        
            
        

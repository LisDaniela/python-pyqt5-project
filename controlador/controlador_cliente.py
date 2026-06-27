from modelo.datos import ManejarJson
from modelo.empresa import Empresa
from vista.datos_cliente import DatosdelCliente

class DatosCliente:
    def __init__(self):
        self.json = ManejarJson()
        self.empresa = Empresa()
        self.v_cliente = DatosdelCliente(self)

    def determinar_cliente(self):
        dicc = self.json.cargar_datos() 
        municipio = self.v_cliente.comboBox.currentText()

        self.v_cliente.label_2.setText("Nombre: ")
        self.v_cliente.label_3.setText("Sexo: ")
        self.v_cliente.label_4.setText("Tipo de entidad: ")
        self.v_cliente.label_5.setText("Direccion: ")
        self.v_cliente.label_6.setText("Datos del Cliente: ")
        self.v_cliente.label_7.setText("Datos del Proyecto: ")
        self.v_cliente.label_8.setText("Nombre: ")
        self.v_cliente.label_10.setText("Código: ")
        self.v_cliente.label_11.setText("Duración: ")
        self.v_cliente.label_validar.setText("")
        self.v_cliente.nombre_cliente.show()
        self.v_cliente.sexo_cliente.show()
        self.v_cliente.entidad_cliente.show()
        self.v_cliente.direccion_cliente.show()
        self.v_cliente.nombre_proyecto.show()
        self.v_cliente.codigo_proyecto.show()
        self.v_cliente.duracion_proyecto.show() 

        cliente, mayor_duracion = self.empresa.determinar_cliente(municipio, dicc)

        if not cliente or not mayor_duracion:
            self.v_cliente.label_validar.setText("No hay proyectos de edificación en ese municipio")
            self.v_cliente.label_validar.setStyleSheet("""
                                QLabel{color: red;
                                        font-size:12pt}
                                               """)
            return

        self.v_cliente.nombre_cliente.setText(cliente["nombre"])
        self.v_cliente.sexo_cliente.setText(cliente["sexo"])
        self.v_cliente.entidad_cliente.setText(cliente["tipo_entidad"])
        direccion_cliente = f"{cliente["direccion"]["calle"]}, #{str(cliente["direccion"]["numero"])}, {cliente["direccion"]["municipio"]}, {cliente["direccion"]["provincia"]}"
        self.v_cliente.direccion_cliente.setText(direccion_cliente)
        self.v_cliente.nombre_proyecto.setText(mayor_duracion["nombre"])
        self.v_cliente.codigo_proyecto.setText(str(mayor_duracion["codigo_identificacion"]))
        self.v_cliente.duracion_proyecto.setText(str(mayor_duracion["duracion"]))

    def mostrar_comboBox(self):
        self.v_cliente.comboBox.show()
        titulo = self.v_cliente.comboBox.itemText(0) if self.v_cliente.comboBox.count() > 0 else "--Seleccione--"
        self.v_cliente.comboBox.blockSignals(True)
        self.v_cliente.comboBox.clear()
        self.v_cliente.comboBox.addItem(titulo)
        self.v_cliente.deseleccionar_titulo_comboBox() 

        dicc = self.json.cargar_datos()
        p_edificacion = [p for p in dicc["Proyectos"] if p["tipo"] == "edificacion"]
        if not p_edificacion:
            self.v_cliente.label.setText("No hay proyectos de edificación actualmente\nPor favor inserte más proyectos")
            self.v_cliente.label.setStyleSheet("""
                                QLabel{color: red;
                                        font-size:16pt}
                                               """)
            self.v_cliente.comboBox.hide()
        else:
            municipios = [pe["direccion"]["municipio"].strip().capitalize() for pe in p_edificacion]
            municipios_sin_repetir = list(set(municipios))
            self.v_cliente.comboBox.addItems(municipios_sin_repetir)
            self.v_cliente.comboBox.blockSignals(False)

            self.v_cliente.label.setText("Seleccione un municipio para determinar los datos del cliente del proyecto de edificación de mayor duración que se desarrolla en dicho municipio:")
            self.v_cliente.label.setStyleSheet("""
                                QLabel{color: black;
                                        font-size:13pt}
                                               """)

    def limpiar(self):
        self.v_cliente.label_validar.setText("")
        self.v_cliente.label_2.setText("")
        self.v_cliente.label_3.setText("")
        self.v_cliente.label_4.setText("")
        self.v_cliente.label_5.setText("")
        self.v_cliente.label_6.setText("")
        self.v_cliente.label_7.setText("")
        self.v_cliente.label_8.setText("")
        self.v_cliente.label_10.setText("")
        self.v_cliente.label_11.setText("")
        self.v_cliente.nombre_cliente.hide()
        self.v_cliente.sexo_cliente.hide()
        self.v_cliente.entidad_cliente.hide()
        self.v_cliente.direccion_cliente.hide()
        self.v_cliente.nombre_proyecto.hide()
        self.v_cliente.codigo_proyecto.hide()
        self.v_cliente.duracion_proyecto.hide()

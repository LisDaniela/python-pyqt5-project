from modelo.empresa import Empresa
from modelo.datos import ManejarJson
from vista.modificar_cumplimiento import Cumplimiento

class ModificarCumplimiento:
    def __init__(self):
        self.json = ManejarJson()
        self.empresa = Empresa()
        self.v_cumplimiento = Cumplimiento(self)

    def diccionario(self):
        dicc = self.json.cargar_datos()
        codigo = self.v_cumplimiento.comboBox.currentText()
        codigo = codigo.split("- ")
        codigo = codigo[0]
        return dicc, codigo

    def validar(self):
        self.v_cumplimiento.label_validar.setText("")
        self.v_cumplimiento.spinBox.show()
        self.v_cumplimiento.label_2.show()
        self.v_cumplimiento.buttonBox.show()
        self.v_cumplimiento.label_3.setText("Nombre: ")
        self.v_cumplimiento.label_6.setText("Cliente: ")
        self.v_cumplimiento.label_8.setText("Arquitecto: ")
        self.v_cumplimiento.label_10.setText("Tipo: ")
        self.v_cumplimiento.label_12.setText("Fecha de inicio: ")
        self.v_cumplimiento.label_14.setText("Cumplimiento actual: ")
        self.v_cumplimiento.nombre_proyecto.show()
        self.v_cumplimiento.cliente_proyecto.show()
        self.v_cumplimiento.arquitecto_proyecto.show()
        self.v_cumplimiento.tipo_proyecto.show()
        self.v_cumplimiento.fecha_proyecto.show()
        self.v_cumplimiento.cumplimiento_actual_proyecto.show()
        dicc, codigo = self.diccionario()

        if dicc["Proyectos"]:
        
            for p in dicc["Proyectos"]:
                if p["codigo_identificacion"] == int(codigo):
                    proyecto = p
                    break
            self.v_cumplimiento.label_texto.setText(f"Escriba el nuevo porcentaje de cumplimiento para el proyecto '{proyecto["nombre"]}':")
            self.v_cumplimiento.nombre_proyecto.setText(proyecto["nombre"])
            self.v_cumplimiento.cliente_proyecto.setText(proyecto["cliente"]["nombre"])
            self.v_cumplimiento.arquitecto_proyecto.setText(proyecto["arquitecto"]["nombre"])
            self.v_cumplimiento.tipo_proyecto.setText(proyecto["tipo"])
            self.v_cumplimiento.fecha_proyecto.setText(proyecto["fecha_inicio"])
            self.v_cumplimiento.cumplimiento_actual_proyecto.setText(str(proyecto["cumplimiento"])+"%")
            cumplimiento_anterior = proyecto["cumplimiento"]
            self.v_cumplimiento.spinBox.setValue(cumplimiento_anterior)

    def modificar_cumplimiento(self):
        dicc, codigo = self.diccionario()
        por_ciento_modificado = self.v_cumplimiento.spinBox.value()
        
        self.empresa.modificar_cumplimiento(dicc, codigo, por_ciento_modificado)
  
        self.limpiar()
        self.v_cumplimiento.label_texto_final.setText(f"Ahora el proyecto de código '{codigo}' tiene un por ciento de cumplimiento del {por_ciento_modificado}%")
        

    def mostrar_comboBox(self):
        self.v_cumplimiento.comboBox.show()
        titulo = self.v_cumplimiento.comboBox.itemText(0) if self.v_cumplimiento.comboBox.count() > 0 else "--Seleccione--"
        self.v_cumplimiento.comboBox.blockSignals(True)
        self.v_cumplimiento.comboBox.clear()
        self.v_cumplimiento.comboBox.addItem(titulo)
        self.v_cumplimiento.deseleccionar_titulo_comoBox()

        dicc = self.json.cargar_datos()
        if not dicc["Proyectos"]:
            self.v_cumplimiento.label.setText("Actualmente no hay ningún proyecto en la base de datos\nPor favor inserte más proyectos")
            self.v_cumplimiento.label.setStyleSheet("""
                                QLabel{color: red;
                                        font-size:16pt}
                                               """)
            self.v_cumplimiento.comboBox.hide()
        else:
            ci = [str(p["codigo_identificacion"]) + "- " + p["nombre"] for p in dicc["Proyectos"]]
            self.v_cumplimiento.comboBox.addItems(ci)
            self.v_cumplimiento.comboBox.blockSignals(False)

            self.v_cumplimiento.label.setText("Seleccione el proyecto:")
            self.v_cumplimiento.label.setStyleSheet("""
                                QLabel{color: black;
                                        qproperty-alignment: AlignLeft;
                                        font-size:16pt}
                                               """)

    def limpiar(self):
        self.v_cumplimiento.spinBox.setValue(0)
        self.v_cumplimiento.label_validar.setText("")
        self.v_cumplimiento.label_texto_final.setText("")
        self.v_cumplimiento.spinBox.hide()
        self.v_cumplimiento.label_2.hide()
        self.v_cumplimiento.buttonBox.hide()
        self.v_cumplimiento.label_3.setText("")
        self.v_cumplimiento.label_6.setText("")
        self.v_cumplimiento.label_8.setText("")
        self.v_cumplimiento.label_10.setText("")
        self.v_cumplimiento.label_12.setText("")
        self.v_cumplimiento.label_14.setText("")
        self.v_cumplimiento.label_texto.setText("")
        self.v_cumplimiento.nombre_proyecto.hide()
        self.v_cumplimiento.cliente_proyecto.hide()
        self.v_cumplimiento.arquitecto_proyecto.hide()
        self.v_cumplimiento.tipo_proyecto.hide()
        self.v_cumplimiento.fecha_proyecto.hide()
        self.v_cumplimiento.cumplimiento_actual_proyecto.hide()

        self.v_cumplimiento.comboBox.blockSignals(True)
        self.v_cumplimiento.comboBox.setCurrentIndex(0)
        self.v_cumplimiento.deseleccionar_titulo_comoBox()
        self.v_cumplimiento.comboBox.blockSignals(False)

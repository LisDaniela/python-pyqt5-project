from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class VistaProyecto(QDialog):
    def __init__(self):
        super(VistaProyecto, self).__init__()
        loadUi("vista/ui/agregar_proyecto.ui", self)
        self.dicc_proyecto = {}
        self.checkBox.setHidden(True)
        self.tipo_vial.toggled.connect(self.cambiar)
        self.fecha_original = self.fecha_de_inicio.date()

        self.buttonBox_proyecto.accepted.connect(self.validar)
        self.buttonBox_proyecto.rejected.connect(self.cerrar_ventana)
        self.rejected.connect(self.cerrar_ventana)

    def cambiar(self):
        if self.tipo_vial.isChecked():
            self.label_altura.setText("Longitud:")
            self.m_o_km.setText("km")
            self.tipo_1.setText("Carretera")
            self.tipo_2.setText("Vías Férreas")
        else:
            self.label_altura.setText("Altura:")
            self.m_o_km.setText("m")
            self.tipo_1.setText("Industrial")
            self.tipo_2.setText("Oficinas")

    def validar(self):
        if not self.list_arquitectos.currentItem() or not self.list_clientes.currentItem():
            QMessageBox.warning(self, "Error", "Debe seleccionar un arquitecto y un cliente")
            return
        if self.nombre_proyecto.text() == "":
            QMessageBox.warning(self, "Error", "Los campos no deben estar vacíos")
        elif not self.nombre_proyecto.text().replace(" ", "").isalnum():
            QMessageBox.warning(self, "Error", "Los campos no deben tener caracteres especiales")
        elif not 0 <= self.cumplimient.value() <= 100:
            QMessageBox.warning(self, "Error", "El porcentaje de cumplimiento debe estar entre 0 y 100")
        elif self.presupuest.value() < 0:
            QMessageBox.warning(self, "Error", "El presupuesto del proyecto no puede ser negativo")
        elif self.duracio.value() <= 0:
            QMessageBox.warning(self, "Error", "La duracion del proyecto no debe ser menor a 0 meses")
        else:
            self.item_arqui = self.list_arquitectos.currentItem()
            if self.item_arqui:
                self.arquiecto = self.item_arqui.data(Qt.UserRole)
            self.item_cliente = self.list_clientes.currentItem()
            if self.item_cliente:
                self.cliente = self.item_cliente.data(Qt.UserRole)
            if self.tipo_edificacion.isChecked():
                if self.calle_proyecto.text() == "" or self.municipio_proyecto.text() == "" or self.prov_proyecto.text() == "":
                    QMessageBox.warning(self, "Error", "Los campos no deben estar vacíos")
                    return
                elif not self.calle_proyecto.text().replace(" ", "").isalnum() or not self.municipio_proyecto.text().replace(" ", "").isalnum() or not self.prov_proyecto.text().replace(" ", "").isalnum():
                    QMessageBox.warning(self, "Error", "Los campos no deben tener caracteres especiales")
                    return
                elif self.num_proyecto.value() == 0:
                    QMessageBox.warning(self, "Error", "El número de la calle no puede ser 0")
                    return
                
                self.tipo = "edificacion"
                self.nombre = self.nombre_proyecto.text()
                self.client = self.cliente
                self.presupuesto = self.presupuest.value()
                fecha = self.fecha_de_inicio.date()
                self.fecha_inicio = fecha.toString("dd-MM-yyyy")
                self.duracion = self.duracio.value()
                self.arquitect = self.arquiecto
            
                self.cumplimiento = self.cumplimient.value()
                self.tipo_especifico = "industrial" if self.tipo_1.isChecked() else "oficinas" if self.tipo_2.isChecked() else "residencia"
                self.altura = self.longitud_o_altura.value()
                # self.direccion = {"calle": self.calle_proyecto.text(), "numero": self.num_proyecto.value(), "municipio": self.municipio_proyecto.text(), "provincia": self.prov_proyecto.text()}
                self.calle = self.calle_proyecto.text()
                self.numero = self.num_proyecto.value()
                self.municipio = self.municipio_proyecto.text()
                self.provincia = self.prov_proyecto.text()
                self.tipo_edificacion.setChecked(True)
                self.calle_proyecto.setText("")
                self.num_proyecto.setValue(1)
                self.municipio_proyecto.setText("")
                self.prov_proyecto.setText("")

                
            else:
                # self.dicc_proyecto = {
                self.tipo = "vial"
                self.nombre = self.nombre_proyecto.text()
                self.client =self.cliente
                self.codigo_identificacion = self.codigo_.text()
                self.presupuesto = self.presupuest.value()
                fecha = self.fecha_de_inicio.date()
                self.fecha_inicio = fecha.toString("dd-MM-yyyy")
                self.duracion = self.duracio.value()
                self.arquitect = self.arquiecto
                self.cumplimiento =self.cumplimient.value()
                self.tipo_especifico = "carretera" if self.tipo_1.isChecked() else "vias ferreas"
                self.longitud = self.longitud_o_altura.value()
                self.dentro_de_provincia = "Si" if self.checkBox.isChecked() else "No"

                self.tipo_vial.setChecked(True)



            self.nombre_proyecto.setText("")
            self.codigo_.setText("")
            self.fecha_de_inicio.setDate(self.fecha_original)
            self.tipo_1.setChecked(True)
            self.presupuest.setValue(1)
            self.duracio.setValue(0)
            self.cumplimient.setValue(0)
            self.longitud_o_altura.setValue(1)
            self.accept()

    def cerrar_ventana(self):
        self.nombre_proyecto.setText("")
        self.codigo_.setText("")
        self.fecha_de_inicio.setDate(self.fecha_original)
        self.tipo_1.setChecked(True)
        self.presupuest.setValue(1)
        self.duracio.setValue(0)
        self.cumplimient.setValue(0)
        self.longitud_o_altura.setValue(1)
        self.tipo_edificacion.setChecked(True)
        self.calle_proyecto.setText("")
        self.num_proyecto.setValue(1)                
        self.municipio_proyecto.setText("")
        self.prov_proyecto.setText("")
        self.close()        
                
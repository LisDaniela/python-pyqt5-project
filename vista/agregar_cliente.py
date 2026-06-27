from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

class VistaCliente(QDialog):
    def __init__(self):
        super(VistaCliente, self).__init__()
        loadUi("vista/ui/agregar_cliente.ui", self)

        self.buttonBox_cliente.accepted.connect(self.validar)
        self.buttonBox_cliente.rejected.connect(self.cerrar_ventana)
        self.rejected.connect(self.cerrar_ventana)

    def validar(self):
        if self.lineEdit_cliente.text() == "" or self.calle_cliente.text() == "" or self.municipio_cliente.text() == "" or self.prov_cliente.text() == "":
            QMessageBox.warning(self, "Error", "Todos los campos deben estar llenos")
        elif self.num_cliente.value() == 0:
            QMessageBox.warning(self, "Error", "El número de la calle no puede ser 0")
        elif not self.lineEdit_cliente.text().replace(" ", "").isalnum() or not self.calle_cliente.text().replace(" ", "").isalnum() or not self.municipio_cliente.text().replace(" ", "").isalnum() or not self.prov_cliente.text().replace(" ", "").isalnum():
            QMessageBox.warning(self, "Error", "Los campos no deben tener caracteres especiales")
        else:
            
            self.nombre = self.lineEdit_cliente.text()
            self.sexo = "masculino" if self.masculino_cliente.isChecked() else "femenino"
            self.calle = self.calle_cliente.text()
            self.numero = self.num_cliente.value()
            self.municipio = self.municipio_cliente.text()
            self.provincia = self.prov_cliente.text()
            self.tipo_entidad = "privada" if self.privada.isChecked() else "estatal"
            
            
            self.lineEdit_cliente.setText("")
            self.femenino_cliente.setChecked(True)
            self.calle_cliente.setText("")
            self.num_cliente.setValue(1)
            self.municipio_cliente.setText("")
            self.prov_cliente.setText("")
            self.accept()
            
    def cerrar_ventana(self):
        self.lineEdit_cliente.setText("")
        self.femenino_cliente.setChecked(True)
        self.calle_cliente.setText("")
        self.num_cliente.setValue(1)
        self.municipio_cliente.setText("")
        self.prov_cliente.setText("")
        self.close()
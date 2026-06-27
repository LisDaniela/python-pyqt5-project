from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

class VistaArquitecto(QDialog):
    def __init__(self):
        super(VistaArquitecto, self).__init__()
        loadUi("vista/ui/agregar_arquitecto.ui", self)
        # self.dicc_arqui = {}
        # self.dicc = tabla.dicc
        self.buttonBox.accepted.connect(self.validar)
        self.buttonBox.rejected.connect(self.cerrar_ventana)
        self.rejected.connect(self.cerrar_ventana)
  
    def validar(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, "Error", "Todos los campos deben estar llenos")
        elif not self.lineEdit.text().replace(" ", "").isalnum():
            QMessageBox.warning(self, "Error", "El nombre no debe tener caracteres especiales")
        else:
            # self.dicc_arqui = {
            self.nombre = self.lineEdit.text()
            self.sexo = "masculino" if self.masculino.isChecked() else "femenino"
            self.exp = self.spinBox.value()
            # self.en_uso = False
        
            self.lineEdit.setText("")
            self.spinBox.setValue(0)
            self.femenino.setChecked(True)
            self.accept()
            # return nombre, sexo, exp
    
    def cerrar_ventana(self):
        self.lineEdit.setText("")
        self.femenino.setChecked(True)
        self.spinBox.setValue(0)
        self.close()        
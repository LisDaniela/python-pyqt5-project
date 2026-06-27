from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class Cumplimiento(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(Cumplimiento, self).__init__()
        loadUi("vista/ui/modificar_cumplimiento.ui", self)

        self.buttonBox.accepted.connect(self.__controlador.modificar_cumplimiento)
        self.buttonBox.rejected.connect(self.__controlador.limpiar)
        self.comboBox.currentIndexChanged.connect(self.__controlador.validar)

    def deseleccionar_titulo_comoBox(self):
        modelo = self.comboBox.model()
        item = modelo.item(0)
        item.setEnabled(False)
        
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class DatosdelCliente(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(DatosdelCliente, self).__init__()
        loadUi("vista/ui/datos_cliente.ui", self)

        self.comboBox.currentIndexChanged.connect(self.__controlador.determinar_cliente)
     
    def deseleccionar_titulo_comboBox(self):
        modelo = self.comboBox.model()
        item = modelo.item(0)
        item.setEnabled(False) 
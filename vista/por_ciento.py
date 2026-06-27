from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class Determinar_por_ciento(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(Determinar_por_ciento, self).__init__()
        loadUi("vista/ui/por_ciento_fuera_provincia.ui", self)

        self.buttonBox.accepted.connect(self.__controlador.calcular_por_ciento)


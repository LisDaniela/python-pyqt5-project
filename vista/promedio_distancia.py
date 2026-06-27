from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

class PromedioDistancia(QDialog):
    def __init__(self):
        
        super(PromedioDistancia, self).__init__()
        loadUi("vista/ui/promedio_distancia.ui", self)
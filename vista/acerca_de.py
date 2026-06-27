from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

class AcercaDe(QWidget):
    def __init__(self):
        super(AcercaDe, self).__init__() 
        loadUi("vista/ui/acerca_de.ui", self)
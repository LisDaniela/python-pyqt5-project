from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class OrdenarPresupuesto(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(OrdenarPresupuesto, self).__init__()
        loadUi("vista/ui/ordenar_presupuesto.ui", self)
        self.todos.toggled.connect(self.__controlador.filtrar_proyecto)
        self.carretera.toggled.connect(self.__controlador.filtrar_proyecto)
        self.vias_ferreas.toggled.connect(self.__controlador.filtrar_proyecto)

        self.tWpresupuesto.setAlternatingRowColors(True)

        
        


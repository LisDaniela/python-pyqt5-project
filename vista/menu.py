from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class Menu(QWidget):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(Menu, self).__init__()
        loadUi("vista/ui/menu.ui", self)
        
        self.atras.clicked.connect(self.__controlador.ir_atras)
        self.pushButton.clicked.connect(self.__controlador.iniciar_lista)
        self.pushButton_cliente.clicked.connect(self.__controlador.datos_del_cliente)
        self.pushButton_por_ciento.clicked.connect(self.__controlador.por_ciento)
        self.pushButton_cumplimiento.clicked.connect(self.__controlador.cumplimiento)
        self.pushButton_presupuesto.clicked.connect(self.__controlador.presupuesto)
        self.pushButton_promedio.clicked.connect(self.__controlador.promedio)
        self.pushButton_acerca_de.clicked.connect(self.__controlador.acerca_de)

        self.atras_2.clicked.connect(self.__controlador.ir_atras)
        self.pushButton_2.clicked.connect(self.__controlador.iniciar_lista)
        self.pushButton_cliente_2.clicked.connect(self.__controlador.datos_del_cliente)
        self.pushButton_por_ciento_2.clicked.connect(self.__controlador.por_ciento)
        self.pushButton_cumplimiento_2.clicked.connect(self.__controlador.cumplimiento)
        self.pushButton_presupuesto_2.clicked.connect(self.__controlador.presupuesto)
        self.pushButton_promedio_2.clicked.connect(self.__controlador.promedio)
        self.pushButton_acerca_de_2.clicked.connect(self.__controlador.acerca_de)

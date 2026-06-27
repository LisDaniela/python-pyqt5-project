from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush


class VentanaPrincipal(QMainWindow):
    def __init__(self, controlador):
        self.__controlador = controlador
        super(VentanaPrincipal, self).__init__()
        loadUi("vista/ui/ventana_principal.ui", self)
        self.fondo = QPixmap('vista/img/edificio2.png')
        
        ruta = "vista/fonts/Playfair Display/static/PlayfairDisplay-BoldItalic.ttf"
        QtGui.QFontDatabase.addApplicationFont(ruta)
        self.setAutoFillBackground(True)
        self.centralwidget.setAutoFillBackground(True)
        
        self.pushButton.clicked.connect(self.__controlador.iniciar_menu)
    
    def resizeEvent(self, event):
        fondo = self.fondo.scaled(self.size(), Qt.IgnoreAspectRatio) 
        paleta = self.palette()
        paleta.setBrush(QPalette.Window, QBrush(fondo))
        self.setPalette(paleta) 

        super().resizeEvent(event)

    def mousePressEvent(self, evento):
        self.__controlador.iniciar_menu()

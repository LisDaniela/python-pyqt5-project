from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from modelo.datos import ManejarJson

class LlenarLista:
    def __init__(self, lista):
        self.json = ManejarJson()
        self.__lista = lista
        self.l_arqui = []
        self.l_cliente = []

    def lista(self):
        self.dicc = self.json.cargar_datos()
        self.__lista.list_arquitectos.clear()
        self.__lista.list_clientes.clear()
        self.l_arqui = []
        self.l_cliente = []
        
        if self.dicc:
            if len(self.dicc["Arquitectos"]) > 0:
                num = 1
                for d in self.dicc["Arquitectos"]:
                    self.text_mostrar_a = f"{num} - {d["nombre"]}"
                    self.l_arqui.append(self.text_mostrar_a)
                    item = QtWidgets.QListWidgetItem(self.text_mostrar_a)
                    item.setData(Qt.UserRole, d)
                    self.__lista.list_arquitectos.addItem(item)
                    num += 1
            if len(self.dicc["Clientes"]) > 0:
                num = 1
                for d in self.dicc["Clientes"]:
                    self.text_mostrar_c = f"{num} - {d["nombre"]}"
                    self.l_cliente.append(self.text_mostrar_c)
                    item = QtWidgets.QListWidgetItem(self.text_mostrar_c)
                    item.setData(Qt.UserRole, d)
                    self.__lista.list_clientes.addItem(item)
                    num += 1
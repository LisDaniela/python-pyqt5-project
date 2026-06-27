from PyQt5 import QtWidgets

class LLenarPresupuesto:
    def __init__(self, tabla):
        self.__tabla = tabla
    
    def llenar_tabla_presupuesto(self, proyectos):
        self.__tabla.tWpresupuesto.setRowCount(0)
        self.__tabla.tWpresupuesto.horizontalHeader().setStretchLastSection(True)

        if len(proyectos) > 0: 
                row = 0
                self.__tabla.tWpresupuesto.setRowCount(len(proyectos))
                for c in proyectos:
                    self.__tabla.tWpresupuesto.setItem(row, 0, QtWidgets.QTableWidgetItem(str(c["codigo_identificacion"])))
                    self.__tabla.tWpresupuesto.setItem(row, 1, QtWidgets.QTableWidgetItem(c["nombre"]))
                    self.__tabla.tWpresupuesto.setItem(row, 2, QtWidgets.QTableWidgetItem(c["tipo"]))
                    cliente = f"{c["cliente"]["nombre"]}"
                    self.__tabla.tWpresupuesto.setItem(row, 3, QtWidgets.QTableWidgetItem(cliente))
                    self.__tabla.tWpresupuesto.setItem(row, 4, QtWidgets.QTableWidgetItem(str(c["presupuesto"])))
                    self.__tabla.tWpresupuesto.setItem(row, 5, QtWidgets.QTableWidgetItem(c["fecha_inicio"]))
                    self.__tabla.tWpresupuesto.setItem(row, 6, QtWidgets.QTableWidgetItem(str(c["duracion"])))
                    arquitecto = f"{c["arquitecto"]["nombre"]}"
                    self.__tabla.tWpresupuesto.setItem(row, 7, QtWidgets.QTableWidgetItem(arquitecto))
                    self.__tabla.tWpresupuesto.setItem(row, 8, QtWidgets.QTableWidgetItem(str(c["cumplimiento"])))
                    self.__tabla.tWpresupuesto.setItem(row, 9, QtWidgets.QTableWidgetItem(c["tipo_especifico"]))
                    self.__tabla.tWpresupuesto.setItem(row, 10, QtWidgets.QTableWidgetItem(str(c["longitud"])))
                    self.__tabla.tWpresupuesto.setItem(row, 11, QtWidgets.QTableWidgetItem(c["dentro_de_provincia"]))
                    self.__tabla.tWpresupuesto.setItem(row, 12, QtWidgets.QTableWidgetItem("-"))
                    self.__tabla.tWpresupuesto.setItem(row, 13, QtWidgets.QTableWidgetItem("-"))
                
                    row +=1
        for i in range(self.__tabla.tWpresupuesto.columnCount()):
             self.__tabla.tWpresupuesto.resizeColumnToContents(i)

from PyQt5 import QtWidgets
from modelo.datos import ManejarJson 

class LLenarTabla:
    def __init__(self, tabla):
        self.json = ManejarJson()
        self.__tabla = tabla
        self.__tabla.todos.setChecked(True)
    def tabla(self, proyectos=None):
        self.dicc = self.json.cargar_datos()
        self.__tabla.tWproyecto.setRowCount(0)
        self.__tabla.tWarquitecto.setRowCount(0)
        self.__tabla.tWcliente.setRowCount(0)
        self.__tabla.tWproyecto.horizontalHeader().setStretchLastSection(True)

        if proyectos is None:
            proyectos = [i for i in self.dicc["Proyectos"] if i["cumplimiento"] < 100]
        if self.dicc:
            if len(self.dicc["Arquitectos"]) > 0:
                row = 0
                self.__tabla.tWarquitecto.setRowCount(len(self.dicc["Arquitectos"]))
                for a in self.dicc["Arquitectos"]:
                    self.__tabla.tWarquitecto.setItem(row, 0, QtWidgets.QTableWidgetItem(a["nombre"]))
                    self.__tabla.tWarquitecto.setItem(row, 1, QtWidgets.QTableWidgetItem(a["sexo"]))
                    self.__tabla.tWarquitecto.setItem(row, 2, QtWidgets.QTableWidgetItem(str(a["experiencia"])))
                    row += 1
            if len(self.dicc["Clientes"]) > 0:
                row = 0
                self.__tabla.tWcliente.setRowCount(len(self.dicc["Clientes"]))
                for b in self.dicc["Clientes"]:
                    self.__tabla.tWcliente.setItem(row, 0, QtWidgets.QTableWidgetItem(b["nombre"]))
                    self.__tabla.tWcliente.setItem(row, 1, QtWidgets.QTableWidgetItem(b["sexo"]))
                    direccion_cliente = f"{b["direccion"]["calle"]}, #{str(b["direccion"]["numero"])}, {b["direccion"]["municipio"]}, {b["direccion"]["provincia"]}"
                    self.__tabla.tWcliente.setItem(row, 2, QtWidgets.QTableWidgetItem(direccion_cliente))
                    self.__tabla.tWcliente.setItem(row, 3, QtWidgets.QTableWidgetItem(b["tipo_entidad"]))
                    row += 1
            if len(self.dicc["Proyectos"]) > 0:
                row = 0
                self.__tabla.tWproyecto.setRowCount(len(proyectos))
                for c in proyectos:
                    self.__tabla.tWproyecto.setItem(row, 0, QtWidgets.QTableWidgetItem(str(c["codigo_identificacion"])))
                    self.__tabla.tWproyecto.setItem(row, 1, QtWidgets.QTableWidgetItem(c["nombre"]))
                    self.__tabla.tWproyecto.setItem(row, 2, QtWidgets.QTableWidgetItem(c["tipo"]))

                    cliente = f"{c["cliente"]["nombre"]}"
                    self.__tabla.tWproyecto.setItem(row, 3, QtWidgets.QTableWidgetItem(cliente))

                    if c["presupuesto"]< 0:
                        c["presupuesto"] = 0
                    self.__tabla.tWproyecto.setItem(row, 4, QtWidgets.QTableWidgetItem(str(c["presupuesto"])))
                    self.__tabla.tWproyecto.setItem(row, 5, QtWidgets.QTableWidgetItem(c["fecha_inicio"]))

                    if c["duracion"] <= 0:
                        c["duracion"] = 1
                    self.__tabla.tWproyecto.setItem(row, 6, QtWidgets.QTableWidgetItem(str(c["duracion"])))

                    arquitecto = f"{c["arquitecto"]["nombre"]}"
                    self.__tabla.tWproyecto.setItem(row, 7, QtWidgets.QTableWidgetItem(arquitecto))

                    if c["cumplimiento"] < 0:
                        c["cumplimiento"] = 0
                    elif c["cumplimiento"] > 100:
                        c["cumplimiento"] = 100
                    self.__tabla.tWproyecto.setItem(row, 8, QtWidgets.QTableWidgetItem(str(c["cumplimiento"])))
                    self.__tabla.tWproyecto.setItem(row, 9, QtWidgets.QTableWidgetItem(c["tipo_especifico"]))
                    if "altura" not in c:
                        self.__tabla.tWproyecto.setItem(row, 10, QtWidgets.QTableWidgetItem(str(c["longitud"])))
                        self.__tabla.tWproyecto.setItem(row, 11, QtWidgets.QTableWidgetItem(c["dentro_de_provincia"]))
                        self.__tabla.tWproyecto.setItem(row, 12, QtWidgets.QTableWidgetItem("-"))
                        self.__tabla.tWproyecto.setItem(row, 13, QtWidgets.QTableWidgetItem("-"))
                    else:
                        self.__tabla.tWproyecto.setItem(row, 10, QtWidgets.QTableWidgetItem("-"))
                        self.__tabla.tWproyecto.setItem(row, 11, QtWidgets.QTableWidgetItem("-"))
                        self.__tabla.tWproyecto.setItem(row, 12, QtWidgets.QTableWidgetItem(str(c["altura"])))
                        direccion_proyecto = f"{c["direccion"]["calle"]}, #{str(c["direccion"]["numero"])}, {c["direccion"]["municipio"]}, {c["direccion"]["provincia"]}"
                        self.__tabla.tWproyecto.setItem(row, 13, QtWidgets.QTableWidgetItem(direccion_proyecto))
                    row +=1

        self.ajustar_columnas(self.__tabla.tWproyecto)
        self.ajustar_columnas(self.__tabla.tWarquitecto)
        self.ajustar_columnas(self.__tabla.tWcliente)

        self.json.guardar_datos(self.dicc)

    def ajustar_columnas(self, tabla):
        for i in range(tabla.columnCount()):
            tabla.resizeColumnToContents(i)
        



    
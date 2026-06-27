from PyQt5.QtWidgets import QDialog, QMenu, QMessageBox
from PyQt5.uic import loadUi

class Tabla(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        super(Tabla, self).__init__()
        loadUi("vista/ui/listar_proyectos.ui", self)
        self.eliminar.clicked.connect(self.elm)
        self.modificar.clicked.connect(self.mod)
        self.todos.toggled.connect(self.__presentador.filtrar_proyecto)
        self.vial.toggled.connect(self.__presentador.filtrar_proyecto)
        self.edificacion.toggled.connect(self.__presentador.filtrar_proyecto)
        self.tWproyecto.itemSelectionChanged.connect(self.limpiar_tabla_p)
        self.tWarquitecto.itemSelectionChanged.connect(self.limpiar_tabla_a)
        self.tWcliente.itemSelectionChanged.connect(self.limpiar_tabla_c)

        self.tWproyecto.setAlternatingRowColors(True)
        self.tWcliente.setAlternatingRowColors(True)
        self.tWarquitecto.setAlternatingRowColors(True)
        
        menu = QMenu()
        self.proyecto = menu.addAction("Proyecto")
        self.arquitecto = menu.addAction("Arquitecto")
        self.cliente = menu.addAction("Cliente")
        self.agregar.setMenu(menu) 

        self.arquitecto.triggered.connect(self.__presentador.agregar)
        self.cliente.triggered.connect(self.__presentador.agregar)
        self.proyecto.triggered.connect(self.__presentador.agregar)

    def elm(self):
        filas_p = self.determinar_filas_seleccionadas(self.tWproyecto)
        filas_a = self.determinar_filas_seleccionadas(self.tWarquitecto)
        filas_c = self.determinar_filas_seleccionadas(self.tWcliente)
        if not self.tWarquitecto.selectedItems() and not self.tWcliente.selectedItems() and not self.tWproyecto.selectedItems():
            QMessageBox.warning(self, "Error", "Debe seleccionar una fila para eliminar")
        elif len(filas_p) > 1 or len(filas_a) > 1 or len(filas_c) > 1:
            QMessageBox.warning(self, "Error", "No debe seleccionar más de una fila para eliminar")
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Confirmar eliminación")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Cancel)

            if self.tWproyecto.selectedItems():
                msg_box.setText("¿Está seguro de que quiere eliminar ese proyecto?")
            elif self.tWarquitecto.selectedItems():
                msg_box.setText("¿Está seguro de que quiere eliminar ese arquitecto?")
            else:
                msg_box.setText("¿Está seguro de que quiere eliminar ese cliente?")



            respuesta = msg_box.exec_()
            if respuesta == QMessageBox.Ok:
                self.__presentador.eliminar()
            
        self.limpiar_todas_tablas()

    def mod(self):
        filas_p = self.determinar_filas_seleccionadas(self.tWproyecto)
        filas_a = self.determinar_filas_seleccionadas(self.tWarquitecto)
        filas_c = self.determinar_filas_seleccionadas(self.tWcliente)
        
        if not self.tWarquitecto.selectedItems() and not self.tWcliente.selectedItems() and not self.tWproyecto.selectedItems():
            QMessageBox.warning(self, "Error", "Debe seleccionar una fila para modificar")
        elif len(filas_p) > 1 or len(filas_a) > 1 or len(filas_c) > 1:
            QMessageBox.warning(self, "Error", "No debe seleccionar más de una fila para modificar")
        else:
            self.__presentador.modificar()
        self.limpiar_todas_tablas()
    
    def determinar_filas_seleccionadas(self, tabla):
        filas = []
        for celda in tabla.selectedItems():
            fila = celda.row()
            if fila not in filas:
                filas.append(fila)
        return filas

    def limpiar_todas_tablas(self):
        self.tWarquitecto.blockSignals(True)
        self.tWarquitecto.clearSelection()
        self.tWarquitecto.blockSignals(False)
        self.tWcliente.blockSignals(True)
        self.tWcliente.clearSelection()
        self.tWcliente.blockSignals(False)
        self.tWproyecto.blockSignals(True)
        self.tWproyecto.clearSelection()
        self.tWproyecto.blockSignals(False)
            
    def limpiar_tabla_p(self):
        self.tWarquitecto.blockSignals(True)
        self.tWarquitecto.clearSelection()
        self.tWarquitecto.blockSignals(False)
        self.tWcliente.blockSignals(True)
        self.tWcliente.clearSelection()
        self.tWcliente.blockSignals(False)


    def limpiar_tabla_a(self):
        self.tWproyecto.blockSignals(True)
        self.tWproyecto.clearSelection()
        self.tWproyecto.blockSignals(False)
        self.tWcliente.blockSignals(True)
        self.tWcliente.clearSelection()
        self.tWcliente.blockSignals(False)


    def limpiar_tabla_c(self):
        self.tWproyecto.blockSignals(True)
        self.tWproyecto.clearSelection()
        self.tWproyecto.blockSignals(False)
        self.tWarquitecto.blockSignals(True)
        self.tWarquitecto.clearSelection()
        self.tWarquitecto.blockSignals(False)


        
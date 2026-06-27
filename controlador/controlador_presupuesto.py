from modelo.empresa import Empresa
from modelo.datos import ManejarJson
from vista.ordenar_presupuesto import OrdenarPresupuesto
from modelo.llenar_presupuesto import LLenarPresupuesto

class ControladorPresupuesto:
    def __init__(self):
        self.json = ManejarJson()
        self.empresa = Empresa()
        self.v_presupuesto = OrdenarPresupuesto(self)
        self.llenar_tabla = LLenarPresupuesto(self.v_presupuesto)

    def ordenar_tabla_presupuesto(self):
        self.v_presupuesto.todos.setChecked(True)
        self.dicc = self.json.cargar_datos()
        self.__viales = []
        for p in self.dicc["Proyectos"]:
            if p["tipo"] == "vial":
                self.__viales.append(p)

        viales = self.empresa.ordenar_presupuestos(self.__viales)
        self.llenar_tabla.llenar_tabla_presupuesto(viales)

    def filtrar_proyecto(self):
        proyectos_filtrados = []
        if self.v_presupuesto.todos.isChecked():
            proyectos_filtrados = self.__viales 
        else:
            if self.v_presupuesto.carretera.isChecked():
                tipo = "carretera"
            if self.v_presupuesto.vias_ferreas.isChecked():
                tipo = "vias ferreas"
            for d in self.__viales:
                if d["tipo_especifico"] == tipo:
                    proyectos_filtrados.append(d)
        viales = self.empresa.ordenar_presupuestos(proyectos_filtrados)
        self.llenar_tabla.llenar_tabla_presupuesto(viales)


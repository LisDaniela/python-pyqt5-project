from modelo.datos import ManejarJson
from modelo.empresa import Empresa
from vista.promedio_distancia import PromedioDistancia

class CalcularPromedio:
    def __init__(self):
        self.json = ManejarJson()
        self.empresa = Empresa()
        self.promedio_v = PromedioDistancia()

    def calcular_promedio(self):
        self.dicc = self.json.cargar_datos()
        promedio = self.empresa.determinar_promedio(self.dicc)

        if promedio == False:
            self.promedio_v.label_promedio.setText("No hay proyectos ferroviarios que hayan sido comenzados en el último año")
            self.promedio_v.label_promedio.setStyleSheet("""
                                QLabel{color: red;}""")
            self.promedio_v.label_3.hide()
        else:
            self.promedio_v.label_promedio.setText(str(promedio))
            self.promedio_v.label_promedio.setStyleSheet("""
                                QLabel{color: black;}""")
            self.promedio_v.label_3.show()


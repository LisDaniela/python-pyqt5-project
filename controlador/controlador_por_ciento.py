from modelo.empresa import Empresa
from modelo.datos import ManejarJson
from vista.por_ciento import Determinar_por_ciento

class PorCiento:
    def __init__(self):
        self.v_por_ciento = Determinar_por_ciento(self)
        self.json = ManejarJson()
        self.empresa = Empresa()

    def calcular_por_ciento(self):
        self.dicc = self.json.cargar_datos()
        valor = self.v_por_ciento.spinBox.value()
        p_viales = self.empresa.determinar_proyectos_viales_mas_distancia(self.dicc, valor)
        
        if not p_viales:
            self.v_por_ciento.label_2.setText("No hay proyectos viales con una longitud más larga a la insertada")
            self.v_por_ciento.label_2.setStyleSheet("""
                                QLabel{color: red;}""")
        else:
            por_ciento = self.empresa.calcular_porcentaje(p_viales)
            self.v_por_ciento.label_2.setText(f"El porcentaje de proyectos viales de más de {valor}km que son fuera de provincia es del {por_ciento:.0f}%")
            self.v_por_ciento.label_2.setStyleSheet("""
                                QLabel{color: black;}""")
            
    def limpiar(self):
        self.v_por_ciento.label_2.setText("")
        self.v_por_ciento.spinBox.setValue(0)
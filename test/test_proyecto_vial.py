from unittest import TestCase
from modelo.proyecto_vial import ProyectoVial

class TestProyectoVial(TestCase):    
    def setUp(self):
        self.cliente = {
            "en_uso": True,
            "id_": 3,
            "nombre": "Luis Fernández",
            "sexo": "masculino",
            "tipo_entidad": "privada"
        }
        self.arquitecto = {
            "en_uso": True,
            "id_": 1,
            "nombre": "Carlos Pérez",
            "sexo": "masculino",
            "experiencia": 15
        }
        self.proyecto_vial = ProyectoVial(
            tipo="vial",
            nombre="Autopista Central Oriente",
            cliente=self.cliente,
            presupuesto=5000000,
            codigo_identificacion=5,
            fecha_inicio="10-02-2024",
            duracion=36,
            arquitecto=self.arquitecto,
            cumplimiento=8,
            tipo_especifico="carretera",
            longitud=350,
            dentro_de_provincia="No"
        )
    
    def test_creacion_proyecto_vial(self):
        self.assertEqual(self.proyecto_vial.tipo, "vial")
        self.assertEqual(self.proyecto_vial.tipo_especifico, "carretera")
    
    def test_proyecto_vial_nombre(self):
        self.assertEqual(self.proyecto_vial.nombre, "Autopista Central Oriente")
    
    def test_proyecto_vial_dict(self):
        diccionario = self.proyecto_vial.diccio()
        self.assertIsInstance(diccionario, dict)
        self.assertIn("tipo_especifico", diccionario)

    def test_proyecto_vial_cumplimiento(self):
        self.assertGreaterEqual(self.proyecto_vial.cumplimiento, 0)
        self.assertLessEqual(self.proyecto_vial.cumplimiento, 100)
    
    def test_proyecto_vial_presupuesto_mayor(self):
        self.assertGreater(self.proyecto_vial.presupuesto, 1000000)
    
    def test_proyecto_vial_duracion_larga(self):
        self.assertGreaterEqual(self.proyecto_vial.duracion, 24)

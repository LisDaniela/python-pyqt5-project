from unittest import TestCase
from modelo.proyecto import Proyectos

class TestProyectos(TestCase):    
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
            "id_": 2,
            "nombre": "Laura Martínez",
            "sexo": "femenino",
            "experiencia": 8
        }
        self.proyecto = Proyectos(
            tipo="edificación",
            nombre="Proyecto Centro Comercial",
            cliente=self.cliente,
            presupuesto=500000,
            codigo_identificacion=25,
            fecha_inicio="15-01-2026",
            duracion=12,
            arquitecto=self.arquitecto,
            cumplimiento=75,
            tipo_especifico="industrial"
        )
    
    def test_creacion_proyecto(self):
        self.assertEqual(self.proyecto.tipo, "edificación")
        self.assertEqual(self.proyecto.nombre, "Proyecto Centro Comercial")
        self.assertEqual(self.proyecto.presupuesto, 500000)
        self.assertEqual(self.proyecto.codigo_identificacion, 25)
    
    def test_proyecto_duracion(self):
        self.assertEqual(self.proyecto.duracion, 12)
        self.assertGreater(self.proyecto.duracion, 0)
    
    def test_proyecto_cumplimiento(self):
        self.assertEqual(self.proyecto.cumplimiento, 75)
        self.assertGreaterEqual(self.proyecto.cumplimiento, 0)
        self.assertLessEqual(self.proyecto.cumplimiento, 100)
    
    def test_proyecto_cliente_asociado(self):
        self.assertEqual(self.proyecto.cliente["nombre"], "Luis Fernández")
        self.assertIn("id_", self.proyecto.cliente)
    
    def test_proyecto_arquitecto_asociado(self):
        self.assertEqual(self.proyecto.arquitecto["nombre"], "Laura Martínez")
        self.assertIn("experiencia", self.proyecto.arquitecto)
    
    def test_proyecto_presupuesto_positivo(self):
        self.assertGreater(self.proyecto.presupuesto, 0)

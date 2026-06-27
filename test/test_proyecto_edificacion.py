from unittest import TestCase
from modelo.proyecto_edificacion import ProyectoEdificacion

class TestProyectoEdificacion(TestCase):
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
        self.proyecto_edif = ProyectoEdificacion(
            tipo="edificación",
            nombre="Edificio Empresarial Centro",
            cliente=self.cliente,
            presupuesto=1000000,
            codigo_identificacion=1,
            fecha_inicio="01-08-2025",
            duracion=16,
            arquitecto=self.arquitecto,
            cumplimiento=62,
            tipo_especifico="oficinas",
            altura=15,
            direccion={"calle": "Calle Central", "numero": 456, "ciudad": "La Habana"}
        )
    
    def test_creacion_proyecto_edificacion(self):
        self.assertEqual(self.proyecto_edif.tipo, "edificación")
        self.assertEqual(self.proyecto_edif.tipo_especifico, "oficinas")
    
    def test_proyecto_edificacion_tipo_especifico(self):
        self.assertIn(self.proyecto_edif.tipo_especifico, 
                     ["residencia", "oficinas", "industrial"])
        
    def test_proyecto_edificacion_cumplimiento(self):
        self.assertGreaterEqual(self.proyecto_edif.cumplimiento, 0)
        self.assertLessEqual(self.proyecto_edif.cumplimiento, 100)
    
    def test_proyecto_edificacion_dict(self):
        diccionario = self.proyecto_edif.diccio()
        self.assertIsInstance(diccionario, dict)
        self.assertIn("tipo", diccionario)
        self.assertIn("nombre", diccionario)
    
    def test_proyecto_edificacion_presupuesto_alto(self):
        self.assertEqual(self.proyecto_edif.presupuesto, 1000000)
        self.assertGreater(self.proyecto_edif.presupuesto, 500000)

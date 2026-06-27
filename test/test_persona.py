from unittest import TestCase
from modelo.persona import Persona

class TestPersona(TestCase):    
    def setUp(self):
        self.persona = Persona(
            id_=5,
            nombre="Juan Pérez",
            sexo="masculino"
        )
    
    def test_creacion_persona(self):
        self.assertEqual(self.persona.id_, 5)
        self.assertEqual(self.persona.nombre, "Juan Pérez")
        self.assertEqual(self.persona.sexo, "masculino")
    
    def test_persona_sexo_valido(self):
        persona_f = Persona(id_=6, nombre="María López", sexo="femenino")
        self.assertEqual(persona_f.sexo, "femenino")
    
    def test_persona_id_positivo(self):
        self.assertGreater(self.persona.id_, 0)
    
    def test_persona_nombre_no_vacio(self):
        self.assertNotEqual(self.persona.nombre, "")
        self.assertIsNotNone(self.persona.nombre)

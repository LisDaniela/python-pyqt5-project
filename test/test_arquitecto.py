from unittest import TestCase
from modelo.arquitecto import Arquitecto

class TestArquitecto(TestCase):
    def setUp(self):
        self.arquitecto = Arquitecto(
            id_=2,
            nombre="Laura Martínez",
            sexo="femenino",
            experiencia=8,
            en_uso=True
        )
    
    def test_creacion_arquitecto(self):
        self.assertEqual(self.arquitecto.id_, 2)
        self.assertEqual(self.arquitecto.nombre, "Laura Martínez")
        self.assertEqual(self.arquitecto.sexo, "femenino")
    
    def test_arquitecto_experiencia(self):
        self.assertEqual(self.arquitecto.experiencia, 8)
        self.assertGreater(self.arquitecto.experiencia, 0)
    
    def test_arquitecto_en_uso(self):
        self.assertTrue(self.arquitecto.en_uso)
    
    def test_arquitecto_diccio(self):
        diccionario = self.arquitecto.diccio()
        self.assertIsInstance(diccionario, dict)
        self.assertIn("nombre", diccionario)
        self.assertIn("experiencia", diccionario)
        self.assertIn("en_uso", diccionario)
    
    def test_arquitecto_valores_en_diccio(self):
        diccionario = self.arquitecto.diccio()
        self.assertEqual(diccionario["nombre"], "Laura Martínez")
        self.assertEqual(diccionario["experiencia"], 8)
    
    def test_arquitecto_inactivo(self):
        arquitecto_inactivo = Arquitecto(
            id_=4,
            nombre="Ana Rodríguez",
            sexo="femenino",
            experiencia=5,
            en_uso=False
        )
        self.assertFalse(arquitecto_inactivo.en_uso)

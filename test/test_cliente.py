from unittest import TestCase
from modelo.cliente import Cliente

class TestCliente(TestCase):
    def setUp(self):
        self.direccion = {
            "calle": "Ignacio Agramonte",
            "numero": 564,
            "municipio": "Camagüey",
            "provincia": "Camagüey"
        }
        self.cliente = Cliente(
            id_=5,
            nombre="Manuel Ortega",
            sexo="masculino",
            direccion=self.direccion,
            tipo_entidad="estatal",
            en_uso=True
        )
    
    def test_creacion_cliente(self):
        self.assertEqual(self.cliente.id_, 5)
        self.assertEqual(self.cliente.nombre, "Manuel Ortega")
        self.assertEqual(self.cliente.sexo, "masculino")
        self.assertEqual(self.cliente.tipo_entidad, "estatal")
    
    def test_cliente_direccion(self):
        self.assertIn("calle", self.cliente.direccion)
        self.assertEqual(self.cliente.direccion["municipio"], "Camagüey")
        self.assertEqual(self.cliente.direccion["provincia"], "Camagüey")
    
    def test_cliente_en_uso(self):
        self.assertTrue(self.cliente.en_uso)
    
    def test_cliente_diccio(self):
        diccionario = self.cliente.diccio()
        self.assertIsInstance(diccionario, dict)
        self.assertIn("nombre", diccionario)
        self.assertIn("direccion", diccionario)
        self.assertIn("tipo_entidad", diccionario)
    
    def test_cliente_inactivo(self):
        cliente_inactivo = Cliente(
            id_=2,
            nombre="Patricia Suárez",
            sexo="femenino",
            direccion=self.direccion,
            tipo_entidad="privada",
            en_uso=False
        )
        self.assertFalse(cliente_inactivo.en_uso)


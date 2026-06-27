import os
import tempfile
import json
from unittest import TestCase
from modelo.datos import ManejarJson

class TestManejarJson(TestCase):
    def test_no_hay_archivo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            carpeta_actual = os.getcwd()
            os.chdir(tmpdir)
            try:
                manejador = ManejarJson()
                resultado = manejador.cargar_datos()

                esperado = {
                    "Proyectos": [],
                    "Arquitectos": [],
                    "Clientes": [],
                    "Proximo codigo": 1,
                }

                self.assertEqual(resultado, esperado)
                self.assertFalse(os.path.exists("datos.json"))
            finally:
                os.chdir(carpeta_actual)

    def test_guardar_y_cargar_datos_con_archivo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            carpeta_actual = os.getcwd()
            os.chdir(tmpdir)
            try:
                manejador = ManejarJson()
                datos = {
                    "Proyectos": ["proyecto1"],
                    "Arquitectos": ["arquitecto1"],
                    "Clientes": ["cliente1"],
                    "Proximo codigo": 99,
                }

                manejador.guardar_datos(datos)
                self.assertTrue(os.path.exists("datos.json"))

                with open("datos.json", "r", encoding="utf-8") as archivo:
                    cargado = json.load(archivo)

                self.assertEqual(cargado, datos)

                cargado_directo = manejador.cargar_datos()
                self.assertEqual(cargado_directo, datos)
            finally:
                os.chdir(carpeta_actual)

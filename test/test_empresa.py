from unittest import TestCase
from unittest.mock import MagicMock, patch
from modelo.empresa import Empresa

class TestEmpresa(TestCase):
    def setUp(self):
        self.inicial = {
            "Proyectos": [],
            "Arquitectos": [],
            "Clientes": [],
            "Proximo codigo": 1,
        }
        patcher = patch("modelo.empresa.ManejarJson")
        self.addCleanup(patcher.stop)
        self.MockManejarJson = patcher.start()

        instance = self.MockManejarJson.return_value
        instance.cargar_datos.return_value = self.inicial.copy()
        instance.guardar_datos = MagicMock()

        self.empresa = Empresa()
        self.instance = instance

    def test_agregar_cliente(self):
        cliente = {
            "id_": 1,
            "nombre": "Ana",
            "sexo": "femenino",
            "direccion": {"municipio": "La Habana"},
            "tipo_entidad": "privada",
            "en_uso": False,
        }
        self.empresa.agregar_cliente(cliente)

        self.assertIn(cliente, self.empresa.dicc["Clientes"])
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_agregar_arquitecto(self):
        arquitecto = {
            "id_": 2,
            "nombre": "Luis",
            "sexo": "masculino",
            "experiencia": 5,
            "en_uso": False,
        }
        self.empresa.agregar_arquitecto(arquitecto)

        self.assertIn(arquitecto, self.empresa.dicc["Arquitectos"])
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_agregar_proyecto(self):
        proyecto = {
            "tipo": "edificación",
            "nombre": "Centro Comercial",
            "cliente": {"id_": 1, "nombre": "Ana"},
            "presupuesto": 120000,
            "codigo_identificacion": "15",
            "fecha_inicio": "01-06-2026",
            "duracion": 12,
            "arquitecto": {"id_": 2, "nombre": "Luis"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
        }

        self.empresa.agregar_proyecto(proyecto, 42)

        self.assertIn(proyecto, self.empresa.dicc["Proyectos"])
        self.assertEqual(self.empresa.dicc["Proximo codigo"], 42)
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_eliminar_elm(self):
        self.empresa.dicc["Clientes"].append("cliente1")
        self.empresa.eliminar_elm("Clientes", 0)

        self.assertEqual(self.empresa.dicc["Clientes"], [])
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_modificar_elm(self):
        self.empresa.dicc["Proyectos"].append("antiguo")
        self.empresa.modificar_elm("Proyectos", 0, "nuevo")

        self.assertEqual(self.empresa.dicc["Proyectos"][0], "nuevo")
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_determinar_cliente(self):
        proyecto = {
            "tipo": "edificacion",
            "nombre": "Centro Comercial",
            "cliente": {"id_": 1, "nombre": "Ana"},
            "presupuesto": 120000,
            "codigo_identificacion": 16,
            "fecha_inicio": "01-06-2026",
            "duracion": 12,
            "arquitecto": {"id_": 2, "nombre": "Luis"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "direccion": {
                "calle": "Felipe",
                "numero": 5,
                "municipio": "Camagüey"
            }
        }
        proyecto2 = {
            "tipo": "edificacion",
            "nombre": "Centro Comercial",
            "cliente": {"id_": 1, "nombre": "Alejandro"},
            "presupuesto": 120000,
            "codigo_identificacion": 16,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Marta"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "direccion": {
                "calle": "Agramonte",
                "numero": 75,
                "municipio": "Camagüey"
            }
        }
        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)

        self.empresa.determinar_cliente("Camagüey", self.empresa.dicc)

        self.assertEqual(self.empresa.dicc["Proyectos"][1]["duracion"], 36)
        self.assertEqual(self.empresa.dicc["Proyectos"][1]["cliente"]["nombre"], "Alejandro")

    def test_determinar_cliente_sin_proyectos(self):
        cliente, proyecto = self.empresa.determinar_cliente("Camagüey", self.empresa.dicc)

        self.assertIsNone(cliente)
        self.assertIsNone(proyecto)

    def test_modificar_cumplimiento(self):
        proyecto = {
            "tipo": "edificación",
            "nombre": "Centro Comercial",
            "cliente": {"id_": 1, "nombre": "Ana"},
            "presupuesto": 120000,
            "codigo_identificacion": 15,
            "fecha_inicio": "01-06-2026",
            "duracion": 12,
            "arquitecto": {"id_": 2, "nombre": "Luis"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "direccion": {
                "calle": "Felipe",
                "numero": 5,
                "municipio": "Camagüey"
            }
        }
        proyecto2 = {
            "tipo": "edificación",
            "nombre": "Centro Comercial",
            "cliente": {"id_": 1, "nombre": "Alejandro"},
            "presupuesto": 120000,
            "codigo_identificacion": 10,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Marta"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "direccion": {
                "calle": "Agramonte",
                "numero": 75,
                "municipio": "Camagüey"
            }
        }
        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)

        self.empresa.modificar_cumplimiento(self.empresa.dicc, "15", 30)
        self.assertEqual(self.empresa.dicc["Proyectos"][0]["cumplimiento"], 30)
        self.instance.guardar_datos.assert_called_with(self.empresa.dicc)

    def test_determinar_proyectos_viales_mas_distancia(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "cliente": {"id_": 1, "nombre": "Ana"},
            "presupuesto": 120000,
            "codigo_identificacion": 15,
            "fecha_inicio": "01-06-2026",
            "duracion": 12,
            "arquitecto": {"id_": 2, "nombre": "Luis"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 250
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "cliente": {"id_": 1, "nombre": "Alejandro"},
            "presupuesto": 120000,
            "codigo_identificacion": 10,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Marta"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 200
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)

        p_viales = self.empresa.determinar_proyectos_viales_mas_distancia(self.empresa.dicc, 200)

        self.assertEqual(p_viales[0]["longitud"], 250)

    def test_calcular_porcentaje(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "cliente": {"id_": 1, "nombre": "Ana"},
            "presupuesto": 120000,
            "codigo_identificacion": 15,
            "fecha_inicio": "01-06-2026",
            "duracion": 12,
            "arquitecto": {"id_": 2, "nombre": "Luis"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 250,
            "dentro_de_provincia": "Si"
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "cliente": {"id_": 1, "nombre": "Alejandro"},
            "presupuesto": 120000,
            "codigo_identificacion": 10,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Marta"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 200,
            "dentro_de_provincia": "No"
        }
        proyecto3 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "cliente": {"id_": 1, "nombre": "Luis"},
            "presupuesto": 120000,
            "codigo_identificacion": 5,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Pedro"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 500,
            "dentro_de_provincia": "No"
        }
        proyecto4 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "cliente": {"id_": 1, "nombre": "Luis"},
            "presupuesto": 120000,
            "codigo_identificacion": 17,
            "fecha_inicio": "01-06-2026",
            "duracion": 36,
            "arquitecto": {"id_": 2, "nombre": "Pedro"},
            "cumplimiento": 0,
            "tipo_especifico": "industrial",
            "longitud": 100,
            "dentro_de_provincia": "No"
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)
        self.empresa.dicc["Proyectos"].append(proyecto3)
        self.empresa.dicc["Proyectos"].append(proyecto4)

        por_ciento = self.empresa.calcular_porcentaje(self.empresa.dicc["Proyectos"])

        self.assertEqual(por_ciento, 75)

    def test_calcular_porcentaje_sin_proyectos(self):
        por_ciento = self.empresa.calcular_porcentaje([])

        self.assertEqual(por_ciento, 0)

    def test_ordenar_presupuestos(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "presupuesto": 5000,
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "presupuesto": 60000,
        }
        proyecto3 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "presupuesto": 120000,
        }
        proyecto4 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "presupuesto": 90000,
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)
        self.empresa.dicc["Proyectos"].append(proyecto3)
        self.empresa.dicc["Proyectos"].append(proyecto4)

        presupuestos = self.empresa.ordenar_presupuestos(self.empresa.dicc["Proyectos"])
        esperado = [proyecto3, proyecto4, proyecto2, proyecto]

        self.assertListEqual(presupuestos, esperado)

    def test_es_bisiesto(self):
        anio1 = 2024
        anio2 = 1900
        anio3 = 2026

        anio_prueba = self.empresa.es_bisiesto(anio1)
        anio_prueba2 = self.empresa.es_bisiesto(anio2) 
        anio_prueba3 = self.empresa.es_bisiesto(anio3)

        self.assertTrue(anio_prueba)
        self.assertFalse(anio_prueba2)
        self.assertFalse(anio_prueba3)

    def test_determinar_promedio_sin_ferros(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "presupuesto": 5000,
            "tipo_especifico": "carreteras"
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "presupuesto": 60000,
            "tipo_especifico": "carreteras"
        }
        proyecto3 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "presupuesto": 120000,
            "tipo_especifico": "carreteras"
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)
        self.empresa.dicc["Proyectos"].append(proyecto3)

        resultado = self.empresa.determinar_promedio(self.empresa.dicc)
        self.assertFalse(resultado)

    def test_determinar_promedio_proyectos_validos(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "longitud": 400,
            "fecha_inicio": "25-05-2026",
            "tipo_especifico": "vias ferreas"
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "longitud": 100,
            "fecha_inicio": "25-08-2025",
            "tipo_especifico": "vias ferreas"
        }
        proyecto3 = {
            "tipo": "vial",
            "nombre": "Autopista Occidental",
            "longitud": 70,
            "fecha_inicio": "25-01-2026",
            "tipo_especifico": "vias ferreas"
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)
        self.empresa.dicc["Proyectos"].append(proyecto3)

        resultado = self.empresa.determinar_promedio(self.empresa.dicc)

        self.assertEqual(resultado, 190)

    def test_determinar_promedio_fuera_rango(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "longitud": 400,
            "fecha_inicio": "25-05-2025",
            "tipo_especifico": "vias ferreas"
        }
        proyecto2 = {
            "tipo": "vial",
            "nombre": "Autopista Sur",
            "longitud": 100,
            "fecha_inicio": "25-08-2024",
            "tipo_especifico": "vias ferreas"
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)

        resultado = self.empresa.determinar_promedio(self.empresa.dicc)
        self.assertFalse(resultado)

    def test_determinar_promedio_lista_vacia(self):
        dicc = {"Proyectos": []}

        resultado = self.empresa.determinar_promedio(dicc)
        self.assertFalse(resultado)

    def test_determinar_promedio(self):
        proyecto = {
            "tipo": "vial",
            "nombre": "Autopista Norte",
            "longitud": 400,
            "fecha_inicio": "25-05-2026",
            "tipo_especifico": "carretera"
        }
        proyecto2 = {
            "tipo": "edificacion",
            "nombre": "Centro Comercial",
            "longitud": 100,
            "fecha_inicio": "25-08-2025",
            "tipo_especifico": "vias ferreas"
        }
        proyecto3 = {
            "tipo": "vial",
            "nombre": "Ferrocaril Occidental",
            "longitud": 70,
            "fecha_inicio": "25-01-2026",
            "tipo_especifico": "vias ferreas"
        }
        proyecto4 = {
            "tipo": "vial",
            "nombre": "Ferrocaril Los Cocos",
            "longitud": 170,
            "fecha_inicio": "01-01-2026",
            "tipo_especifico": "vias ferreas"
        }

        self.empresa.dicc["Proyectos"].append(proyecto)
        self.empresa.dicc["Proyectos"].append(proyecto2)
        self.empresa.dicc["Proyectos"].append(proyecto3)
        self.empresa.dicc["Proyectos"].append(proyecto4)

        resultado = self.empresa.determinar_promedio(self.empresa.dicc)
        self.assertEqual(resultado, 120)


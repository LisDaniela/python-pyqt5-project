from operator import itemgetter
from datetime import datetime, timedelta
from modelo.datos import ManejarJson

class Empresa:
    def __init__(self):
        self.json = ManejarJson()
        self.dicc = self.json.cargar_datos() 

    def agregar_proyecto(self, proyecto, ultimo_ci):
        self.dicc["Proyectos"].append(proyecto)
        self.dicc["Proximo codigo"] = ultimo_ci
        self.json.guardar_datos(self.dicc)

    def agregar_arquitecto(self, arquitecto):
        self.dicc["Arquitectos"].append(arquitecto)
        self.json.guardar_datos(self.dicc) 

    def agregar_cliente(self, cliente):
        self.dicc["Clientes"].append(cliente)
        self.json.guardar_datos(self.dicc)

    def eliminar_elm(self, tipo, fila):
        del self.dicc[tipo][fila]
        self.json.guardar_datos(self.dicc)

    def modificar_elm(self, tipo, fila, elm_nuevo):
        self.dicc[tipo][fila] = elm_nuevo
        self.json.guardar_datos(self.dicc)

    def determinar_cliente(self, municipio, dicc):
        p_edificacion = [p for p in dicc["Proyectos"] if p["tipo"] == "edificacion"]
        mismo_municipio = [pe for pe in p_edificacion if pe["direccion"]["municipio"].strip().capitalize() == municipio]
        if not mismo_municipio:
            return None, None
        lista = sorted(mismo_municipio, key=itemgetter("duracion"), reverse=True)
        mayor_duracion = lista[0]
        cliente = mayor_duracion["cliente"]
        return cliente, mayor_duracion
    
    def modificar_cumplimiento(self, dicc, codigo, por_ciento_modificado):
        ci = [str(i["codigo_identificacion"]) for i in dicc["Proyectos"]]
        indice = ci.index(codigo)
        dicc["Proyectos"][indice]["cumplimiento"] = por_ciento_modificado
        self.json.guardar_datos(dicc)

    def determinar_proyectos_viales_mas_distancia(self, dicc, valor):
        p_viales = [dicc["Proyectos"][p] for p in range(len(dicc["Proyectos"])) if dicc["Proyectos"][p]["tipo"] == "vial" and dicc["Proyectos"][p]["longitud"] > valor]
        if not p_viales:
            return False
        else:
            return p_viales

    def calcular_porcentaje(self, p_viales):
        if not p_viales:
            return 0
        parte = [v for v in p_viales if v["dentro_de_provincia"] == "No"]
        por_ciento = len(parte) * 100/len(p_viales) 
        return por_ciento
    
    def ordenar_presupuestos(self, proyectos):
        viales = sorted(proyectos, key=itemgetter("presupuesto"), reverse=True)
        return viales

    def es_bisiesto(self, anio):
        if anio % 4 == 0 and anio % 100 != 0:
            return True
        elif anio % 400 == 0:
            return True
        else: 
            return False
        
    def determinar_promedio(self, dicc):
        fecha_hoy = datetime.now().date()
        
        if self.es_bisiesto(int(fecha_hoy.year)) and fecha_hoy.month > 2 or self.es_bisiesto(int(fecha_hoy.year - 1)) and fecha_hoy.month <= 2: 
            fecha_inicial = fecha_hoy - timedelta(days=366)
        else:
            fecha_inicial = fecha_hoy - timedelta(days=365)

        lista_ferros = []
        for proyecto in dicc["Proyectos"]:
            if proyecto["tipo"] == "vial" and proyecto["tipo_especifico"] == "vias ferreas":
                lista_ferros.append(proyecto)

        lista_nueva  =[]
        for i in lista_ferros:
            fecha_proyecto = datetime.strptime(i["fecha_inicio"], "%d-%m-%Y").date()
            if fecha_inicial <= fecha_proyecto <= fecha_hoy:
                lista_nueva.append(i)
         
        longitudes = [p["longitud"] for p in lista_nueva]
        try:
            promedio = sum(longitudes)/len(longitudes)
        except ZeroDivisionError:
            return False
        else:
            return promedio

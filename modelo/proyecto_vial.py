from modelo.proyecto import Proyectos

class ProyectoVial(Proyectos):
    def __init__(self, tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, longitud, dentro_de_provincia):
        super().__init__(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico)
        self.__longitud = longitud
        self.__dentro_de_provincia = dentro_de_provincia

    @property
    def longitud(self):
        return self.__longitud

    @property
    def dentro_de_provincia(self):
        return self.__dentro_de_provincia
    
    def diccio(self):
        dicc = {
        "tipo": self.tipo,
        "nombre": self.nombre,
        "cliente": self.cliente,
        "presupuesto": self.presupuesto,
        "codigo_identificacion": self.codigo_identificacion,
        "fecha_inicio": self.fecha_inicio,
        "duracion": self.duracion,
        "arquitecto": self.arquitecto,
        "cumplimiento": self.cumplimiento,
        "tipo_especifico": self.tipo_especifico,
        "longitud": self.longitud,
        "dentro_de_provincia": self.dentro_de_provincia
        }
        return dicc
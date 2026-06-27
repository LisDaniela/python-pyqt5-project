from modelo.proyecto import Proyectos

class ProyectoEdificacion(Proyectos):
    def __init__(self, tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico, altura, direccion):
        super().__init__(tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico)
        self.__altura = altura
        self.__direccion = direccion

    @property
    def altura(self):
        return self.__altura

    @property
    def direccion(self):
        return self.__direccion
    
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
        "altura": self.altura,
        "direccion": self.direccion
        }
        return dicc
class Proyectos:
    def __init__(self, tipo, nombre, cliente, presupuesto, codigo_identificacion, fecha_inicio, duracion, arquitecto, cumplimiento, tipo_especifico):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__cliente = cliente
        self.__presupuesto = presupuesto
        self.__codigo_identificacion = codigo_identificacion
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__arquitecto = arquitecto
        self.__cumplimiento = cumplimiento
        self.__tipo_especifico = tipo_especifico

    @property
    def tipo(self):
        return self.__tipo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def presupuesto(self):
        return self.__presupuesto
    
    @property
    def codigo_identificacion(self):
        return self.__codigo_identificacion
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @property
    def duracion(self):
        return self.__duracion
    
    @property
    def arquitecto(self):
        return self.__arquitecto
    
    @property
    def cumplimiento(self):
        return self.__cumplimiento
    
    @property
    def tipo_especifico(self):
        return self.__tipo_especifico
    


        
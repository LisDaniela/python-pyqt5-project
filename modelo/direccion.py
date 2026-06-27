class Direccion:
    def __init__(self, calle, numero, municipio, provincia):
        self.__calle = calle
        self.__numero = numero
        self.__municipio = municipio
        self.__provincia = provincia

    @property
    def calle(self):
        return self.__calle

    @property
    def numero(self):
        return self.__numero
    
    @property
    def municipio(self):
        return self.__municipio

    @property
    def provincia(self):
        return self.__provincia
    
    def diccio(self):
        dicc = {
            "calle": self.calle,
            "numero": self.numero,
            "municipio": self.municipio,
            "provincia": self.provincia,
        }
        return dicc



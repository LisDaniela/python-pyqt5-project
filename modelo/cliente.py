from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, id_, nombre, sexo, direccion, tipo_entidad, en_uso=False):
        super().__init__(id_, nombre, sexo, en_uso)
        self.__direccion = direccion
        self.__tipo_entidad = tipo_entidad

    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def tipo_entidad(self):
        return self.__tipo_entidad
    
    
    def diccio(self):
        dicc = {
            "id_": self.id_,
            "nombre": self.nombre,
            "sexo": self.sexo,
            "direccion": self.direccion,
            "tipo_entidad": self.tipo_entidad,
            "en_uso": self.en_uso
        }
        return dicc

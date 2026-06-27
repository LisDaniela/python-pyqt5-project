from modelo.persona import Persona

class Arquitecto(Persona):
    def __init__(self, id_, nombre, sexo, experiencia, en_uso=False):
        super().__init__(id_, nombre, sexo, en_uso)
        self.__experiencia  = experiencia

    @property
    def experiencia(self):
        return self.__experiencia
    
    
    def diccio(self):
        dicc = {
            "id_": self.id_,
            "nombre": self.nombre,
            "sexo": self.sexo,
            "experiencia": self.experiencia,
            "en_uso": self.en_uso
        }
        return dicc
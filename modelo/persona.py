class Persona:
    def __init__(self, id_, nombre, sexo, en_uso=False):
        self.__id_ = id_
        self.__nombre = nombre
        self.__sexo = sexo
        self.__en_uso = en_uso

    @property
    def id_(self):
        return self.__id_
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def en_uso(self):
        return self.__en_uso
    

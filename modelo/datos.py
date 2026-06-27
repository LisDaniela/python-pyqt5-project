import json

class ManejarJson:
    def __init__(self):
        pass        
 
    def guardar_datos(self, datos):
        with open("datos.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)

    def cargar_datos(self):
        try:
            with open("datos.json", "r", encoding="utf-8") as f:
                self.dicc = json.load(f)
                
                return self.dicc
        except (FileNotFoundError, json.JSONDecodeError):
            self.dicc = {"Proyectos": [], "Arquitectos": [], "Clientes": [], "Proximo codigo": 1}
            return self.dicc 
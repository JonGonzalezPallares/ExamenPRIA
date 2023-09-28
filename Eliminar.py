import json
class Eliminar():
    def comprobarDni(self, dni):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        for dato in datos:
            if dato.get('dni')==dni:
                return True            
        else: 
             return False

    
    def recogerIndice(self, dni):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        
        x=0
        for x, dato in enumerate(datos):
            if dato.get('dni')==dni:
                return x
        
    def eliminar(self, dni):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)    
        if self.comprobarDni(dni):
            elimi=datos.pop(self.recogerIndice(dni))
            with open("datos.json", "w") as archivo:
                json.dump(datos, archivo)
            return True
        else: 
            return False
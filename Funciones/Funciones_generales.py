import json
class Funciones():
      def comprobarDni(self, id):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        for dato in datos:
            if dato.get('dni')==dni:
                return True            
        else: 
             return False

    
      def recogerIndice(self, id):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        
        x=0
        for x, dato in enumerate(datos):
            if dato.get('dni')==dni:
                return x
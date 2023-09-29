#Imports
import json
import datetime

#Funciones generales
class Funciones():
    #Funcion para comprobar si existe
    def comprobarDni(self, id):
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
        for dato in datos:
            if dato.get('dni') == dni:
                return True
        else:
            return False

    #Para recoguer el ID
    def recogerIndice(self, id):
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)

        x = 0
        for x, dato in enumerate(datos):
            if dato.get('dni') == dni:
                return x
            
    #Funcion para validar fechas
    def validarFecha(fecha_str):
        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return

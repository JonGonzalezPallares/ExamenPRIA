import json
import datetime as dt
from datetime import datetime
class Funciones_generales():
      def leer_archivo(fichero):
          with open(fichero, "r") as archivo:
            datos= json.load(archivo)
            return datos
      def comprobarDni(self, id):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        for dato in datos:
            if dato.get('id')==id:
                return True            
        else: 
             return False

    
      def recogerIndice(self, id):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        
        x=0
        for x, dato in enumerate(datos):
            if dato.get('id')==id:
                return x
      def ordernar_fechas(vuelos):
          vuelos_ordenados = sorted(vuelos, key=lambda x: x['fecha'])
          for i, fechas in enumerate(vuelos_ordenados):
              fechas['fecha']= dt.datetime.fromtimestamp(fechas['fecha']).strftime('%Y-%m-%d %H:%M:%S')
              vuelos_ordenados[i]['fecha']=fechas['fecha']  
          return vuelos_ordenados

    
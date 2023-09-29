from prettytable import PrettyTable
import json
import os
import Funciones.Funciones_generales as fg

class Leer():
   def __init__(self):
      self.fun=fg.Funciones.ordernar_fechas
      self.l=fg.Funciones.leer_archivo

   def mostrar(self):
      #Para guardar datos en un json
      if(os.path.exists("vuelos.json")):
         datos= fg.Funciones.leer_archivo("vuelos.json")
         print(datos)
         #datos= fg.Funciones.ordernar_fechas(datos)
         print("Fecha de salida\t Id vuelo \t Destino \t Plazas libres")
         for dato in datos:
            print(datos[dato])
      else:
         print("No existe")
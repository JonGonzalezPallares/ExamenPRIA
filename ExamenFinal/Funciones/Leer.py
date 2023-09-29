from prettytable import PrettyTable
import json
import Funciones_generales as fg

class Leer():
    def __init__(self):
       self.fun=fg.Funciones_generales.ordernar_fechas
       self.l=fg.Funciones_generales.leer_archivo
    def leerDatos(self):
      datos= self.l("vuelos.json")
      datos= self.fun(datos)
      print("Fecha de salida\t Id vuelo \t Destino \t Plazas libres")
      for dato in datos:
                
       print(dato['fecha'], "\t", dato['id'], "\t", dato['destino'], "\t", dato['plazas'])
     
leer=Leer()
leer.leerDatos()
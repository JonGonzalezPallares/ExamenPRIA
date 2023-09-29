import prettytable
from prettytable import ALL as ALL
import json
import Funciones.Funciones_generales as fg
import os

class Leer():
   def leerDatos():
      if(os.path.exists("vuelos.json")):
         items_table = prettytable.PrettyTable(hrules=ALL)
         items_table.field_names = ["Fecha salida", "Id", "Destino", "Plazas libres"]
             #Cargamos los datos del json que queremos
         with open("vuelos.json", "r") as read_file:
            items = json.load(read_file)
         #Recorremos los datos
         for item in items:
            items_table.add_row([item["fecha"], item["id"], item["destino"], item["plazas"]])
         print(items_table)
      else:
         print("mal")

#print(dato['fecha'], "\t", dato['id'], "\t", dato['destino'], "\t", dato['plazas'])

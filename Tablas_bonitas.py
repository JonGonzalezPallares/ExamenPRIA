#Para usar las prettytable

#Comando: python -m pip install -U prettytable

import prettytable
from prettytable import ALL as ALL


#Importamos el json
import json
#Importamos el datetime
import datetime

#Creamos una tabla para los elementos
items_table = prettytable.PrettyTable(hrules=ALL)

#Les damos nombre a las columnas
items_table.field_names = ["DNI", "NOMBRE", "APELLIDO", "FECHA", "EDAD"]

#Cargamos los datos del json que queremos
with open("datos.json", "r") as read_file:
    items = json.load(read_file)

#Recorremos los datos
for item in items:
    #Pasamos la fecha de unix a normal
    item["fecha"] = datetime.datetime.fromtimestamp(int(item["fecha"])).strftime('%Y-%m-%d %H:%M:%S')
    #Añadimos todos los datos a la tabla
    items_table.add_row([item["dni"], item["nombre"], item["apellido"], item["fecha"], int(item["edad"])])

#Mostramos por consola la tabla
print(items_table)
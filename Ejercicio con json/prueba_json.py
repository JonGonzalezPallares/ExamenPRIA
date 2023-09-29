#!/usr/bin/env python3

print("Guardar cosas en un JSON")

#Importamos el json
import json
#Importamos los calendarios
import calendar
import datetime

#Recogemos la fecha actual
date = datetime.datetime.utcnow()
#Lo convertimos a tiempo unix
utc_time = calendar.timegm(date.utctimetuple())
utc_time2 = utc_time+23

datos = [
    {
        "dni": "12233423N",
        "nombre": "Jon",
        "apellido": "Gonzalez",
        "fecha": str(utc_time),
        "edad": "23"
    },
    {
        "dni": "23333A",
        "nombre": "Nombre",
        "apellido": "Apellido",
        "fecha": str(utc_time2),
        "edad": "14"
    },
]


#Para guardar datos en un json separado
with open("datos.json", "w") as write_file:
    #json.dump usa dos argumentos: el objeto a serializar y el archivo en el que se va a escribir
    json.dump(datos, write_file)
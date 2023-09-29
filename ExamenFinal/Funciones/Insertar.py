#Imports
import json
import calendar
import datetime as dt
from datetime import datetime
import Funciones.Funciones_generales as fg
import os
import time

vuelo = {
        "fecha": 0,
        "id": 0,
        "destino": "",
        "plazas": 0
    }

#Para cambiar el texto de fecha incorrecta
prueba = False

#Funcion para comprobar si la fecha es correcta o no
def seleccionar_fecha(prueba):
    while True:
        if(prueba):
            fecha = input("\nFecha incorrecta (Formato = YYYY-MM-DD HH:mm:ss): \n")
        else:
            fecha = input("\nIntroduzca la fecha de salida (Formato = YYYY-MM-DD HH:mm:ss): \n")
        start = fg.Funciones.validar_fecha(fecha)

        if(start is not None):
            fecha = time.mktime(dt.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").timetuple())
            vuelo["fecha"]=fecha
            prueba = False
            break
        else:
            prueba = True

#Funcion para comprobar si el destino contiene algun numero
def numeroDestino(prueba):
    while True:
        if(prueba):
            destino = input("\nNo existe ningun destino con numeros, vuelva a intentarlo: \n")
        else:
            destino = input("\nIntroduzca el destino al que va a ir: \n")

        if(any(chr.isdigit() for chr in destino)):
            prueba=True
        else:
            vuelo["destino"]=destino
            prueba=False
            break

#Funcion para comprobar que las plazas sean un numero
def numeroPlazas(prueba):
    while True:
        if(prueba):
            plazas = input("\nDebe introducir un numero entero: \n")
        else:
            plazas = input("\nIntroduzca el numero de plazas: \n")

        if(plazas.isdigit()):
            vuelo["plazas"]=int(plazas)
            prueba=False
            break
        else:
            prueba=True

class Insertar:
    #Funcion para añadir un nuevo vuelo
    def AgregarVuelo():
        #Recogemos la fecha actual
        date = dt.datetime.utcnow()
        #Lo convertimos a tiempo unix
        utc_time = calendar.timegm(date.utctimetuple())
        vuelo["id"]=utc_time
        #Se le pasa la variable de prueba para comprobar el mensaje a mostrar
        seleccionar_fecha(prueba)
        numeroDestino(prueba)
        numeroPlazas(prueba)
        
        #Para guardar datos en un json
        if(os.path.exists("vuelos.json")):
            with open("vuelos.json", "r") as read_file:
                datosTodos = json.load(read_file)
            datosNuevo = [datosTodos]
            datosNuevo.append(vuelo)
            with open("vuelos.json", "w") as archivo:
                json.dump(datosNuevo, archivo)
        else:
            with open("vuelos.json", "w") as archivo:
                json.dump(vuelo, archivo)
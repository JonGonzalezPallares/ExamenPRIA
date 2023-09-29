import json
class Agregar():
    def __init__(self):
       pass
    def agregar(self, persona):
        with open("datos.json", "r") as archivo:
            datos=json.load(archivo)
        datosNew= [datos]
        datosNew.append(persona)
        with open("datos.json", "w") as archivo:
            json.dump(datosNew, archivo)
    
    """dniV= input("Introduzca el dni\n")
    nombreV= input("Introduce el nombre\n")
    edadV= input("Introduce la edad\n")
    ciudadV= input("Introduce la ciudad\n")
    emailV= input("Introduce el email\n")"""

    """datos= { "dni": dniV, "nombre": nombreV, "edad": edadV, "ciudad": ciudadV, "email": emailV}

    agregar(datos)"""
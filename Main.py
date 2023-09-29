#Imports de las clases
import Funciones.Agregar as Agregar
import Funciones.Eliminar as Eliminar
import Funciones.Leer as Leer
import Vista
class Main():
    def __init__(self):
        self.agre=Agregar()
        self.eli=Eliminar()
        self.visu=Leer()
        self.vist=Vista()
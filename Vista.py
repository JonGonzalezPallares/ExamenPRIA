import math
from Funciones.Agregar import Agregar
from Funciones.Eliminar import Eliminar
from Funciones.Leer import Leer

class Vista():
    def __init__(self):
        self.agregar = Agregar()
        self.eliminar = Eliminar()
        self.leer = Leer()

    def elegirAccion(self):
        accion = input("¿Cual eliges?")

        match accion:
            case "0":
                exit()
                pass
            case "1":
                self.agregarVista()
                pass
            case "2":
                self.eliminar.eliminar(0)
               # self.eli.eliminar()
                pass
            case "3":
                # Modificar
                pass
            case "4":
               # self.visu.leer()
                pass
            case _:
                print("Opción no disponible")
                self.pintarTeclado()

    def pintarTeclado(self):
        print("Bienvenido al CRUD  que accion deseas realizar")
        print("0: Salir")
        print("1: Agregar")
        print("2: Eliminar")
        print("3: Modificar")
        print("4: Visualizar")
        self.elegirAccion()


vista1 = Vista()
vista1.pintarTeclado()
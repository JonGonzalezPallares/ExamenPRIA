from Agregar import Agregar
from Eliminar import Eliminar
from Leer import Leer
class Vista():
    def __init__(self):
         self.agregar=Agregar()
         self.eliminar=Eliminar()
         self.leer=Leer()

    def elegirAccion(self):
            accion= input("¿Cual eliges?")

            match accion:
                case "0":
                    exit()
                    pass
                case "1":
                    # self.visu.leer()
                    pass
                case "2":
                    self.agregarVista()
                    pass
                case "3":
                    #Modificar
                    pass
                case "4":
                    # self.eli.eliminar()
                    pass
                case _:
                    print("Opción no disponible")
                    self.pintarTeclado()

    def pintarTeclado(self):
            print("Bienvenido al aeropuerto de Bilbao que accion deseas realizar")
            print("1: Información de los vuelos")
            print("2: Añadir un vuelo")
            print("3: Modificar un vuelo existente")
            print("4: Borrar un vuelo")
            print("0: Salir")
            self.elegirAccion()

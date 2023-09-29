from Funciones.Insertar import Insertar
from Funciones.Eliminar import Eliminar
from Funciones.Leer import Leer
from Funciones.Modificar import Modificar


class Vista():
    def __init__(self):
        self.insertar = Insertar
        self.eliminar = Eliminar
        self.leer = Leer
        self.modificar = Modificar
        
    def elegirAccion(self):
        accion = input("¿Cual eliges?\n")

        match accion:
            case "0":
                exit()
            case "1":
                self.leer.mostrar(self)
            case "2":
                self.insertar.AgregarVuelo()
            case "3":
                self.modificar.modificar(self)
                pass
            case "4":
                #self.eliminar.eliminar()
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

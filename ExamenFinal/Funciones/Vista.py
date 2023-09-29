from Funciones.Insertar import Insertar
from Funciones.Eliminar import Eliminar
from Funciones.Leer import Leer


class Vista():
    def __init__(self):
        self.insertar = Insertar.AgregarVuelo
        self.eliminar = Eliminar
        self.leer=Leer.leerDatos
        
    def elegirAccion(self):
        accion = input("¿Cual eliges?")

        match accion:
            case "0":
                exit()
            case "1":
                self.leer()
                pass
            case "2":
                self.insertar()
            case "3":
                # Modificar
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

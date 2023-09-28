import math
from Agregar import Agregar
from Eliminar import Eliminar
from Leer import Leer


class Vista():
    def __init__(self):
        self.agregar = Agregar()
        self.eliminar = Eliminar()
        self.leer = Leer()

    def agregarVista(self):
        dniV = input("Introduzca el dni\n")
        if len(dniV) > 0 and len(dniV) == 9:
            nombreV = input("Introduce el nombre\n")
            if len(nombreV) > 3:
                edadV = input("Introduce la edad\n")
                if len(edadV) > 0 and isinstance(int(edadV), int):
                    ciudadV = input("Introduce la ciudad\n")
                    if len(ciudadV) > 3:
                        emailV = input("Introduce el email\n")
                        if len(emailV) > 3:
                            datos = {"dni": dniV, "nombre": nombreV,
                                     "edad": edadV, "ciudad": ciudadV, "email": emailV}
                            self.agregar.agregar(datos)
                        else:
                            print("Email no valido, retrocediendo...")
                    else:
                        print("Ciudad no valida, retrocediendo...")
                else:
                    print("Edad no valida, retrocediendo...")
            else:
                print("nombre no valido, retrocediendo...")
                self.pintarTeclado()
        else:
            print("Dni no valido, retrocediendo...")
            self.pintarTeclado()

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

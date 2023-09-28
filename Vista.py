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
        dni = input("Introduzca el dni\n")
        if len(dni) > 0 and len(dni) == 9:
            nombre = input("Introduce el nombre\n")
            if len(nombre) > 3 and nombre.replace(" ","").isalpha():
                edad = input("Introduce la edad\n")
                if len(edad) > 0 and isinstance(int(edad), int):
                    ciudad = input("Introduce la ciudad\n")
                    if len(ciudad) > 3 and ciudad.replace(" ","").isalpha():
                        email = input("Introduce el email\n")
                        if len(email) > 3:
                            datos = {"dni": dni, "nombre": nombre.title(),
                                     "edad": edad, "ciudad": ciudad.title(), "email": email}
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
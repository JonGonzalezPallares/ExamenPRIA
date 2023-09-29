from Agregar import Agregar
from Eliminar import Eliminar
from Leer import Leer
class Vista():
    def __init__(self):
         self.agregar=Agregar()
         self.eliminar=Eliminar()
         self.leer=Leer()

    def agregarVista(self):

        id=input("Introduzca el Numero de vuelo")
        if len(id)>0 and isinstance(int(id), int):
            destino=input("Introduzca el destino del vuelo")
            if len(destino)>3:
                fecha=input("Introduzca el horario de salida")
                if(fecha):
                    plazas=input("Introduzca el numero de plazas libres")
                    if len(plazas)>1 and isinstance(int(plazas), int):
                        datos= {"NumeroVuelo": id, "DestinoVuelo": destino, "HoraSalida": fecha, "NumPlazas": plazas}
                        self.agregar.agregar(datos)
                    else:
                        print("Numero de plazas no valido")
                else:
                    print("Horario no valido...")
            else:
                print("Destino no valido...")
        else:
            print("Id de vuelo no valido")




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

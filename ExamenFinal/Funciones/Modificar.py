import json
import Funciones.Funciones_generales as fg
import Funciones.Vista as vist
class Modificar():
    def __init__(self):
        self.comp=fg.Funciones.comprobarDni
        self.ind=fg.Funciones.recogerIndice
        self.l=fg.Funciones.leer_archivo
        self.pintar=vist.Vista.pintarTeclado

    def modificar(self):
        datos= self.l("vuelos.json")
        error= False

        id= input("Id del vuelo que quieres modificar\n")
        if self.comp(id):
           accion= input("Cual campo quieres modificar 1 para plazas 2 para el destino\n")
           x= self.ind(id)
           if accion=='1':
              nuevoDato= input("Introduce el numero de plazas")
              datos[x]['plazas']==nuevoDato
           elif accion=='2':
              nuevoDato== input("Introduce el destino")
              datos[x]['destino']==nuevoDato
           else:
              print("accion no disponible")
              error=True
        else:
           print("El id no existe") 
           error=True
        if error:
           self.pintar
           

       
    




        
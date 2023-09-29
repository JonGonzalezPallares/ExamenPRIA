import json

class Eliminar():

    def eliminar(self, vueloid):
        with open("vuelos.json", "r") as archivo:
            datos = json.load(archivo)
        correcto = False
        x = 0
        for i, dato in enumerate(datos):
            print(i)
            print(dato)
            if dato.get('id') == vueloid:
                x = i
                correcto = True
                break
        else:
            correcto = False

        if correcto:
            elimi = datos.pop(x)
            with open("vuelos.json", "w") as archivo:
                json.dump(datos, archivo)

            print("El vuelo con ID {vueloid} ha sido eliminado.")
        else:
            print("No se encontró un vuelo con el ID proporcionado")

#Comprobacion que el ID del vuelo es en formato correcto (solo numeros es EPOCH)
while True:
    vueloid_entrada = int(input("Indique ID del vuelo a eliminar:\n"))
    if vueloid_entrada.isdigit():
        vueloid = int(vueloid_entrada)
        break
    else:
        print("Introduzca un ID correcto por favor.")

eliminar_obj = Eliminar()
eliminar_obj.eliminat(vueloid)
import json
class Eliminar():
    
    def eliminar(self, dni):
        with open("datos.json", "r") as archivo:
            datos= json.load(archivo)
        correcto=False
        x=0
        for i, dato in enumerate(datos):

            if dato.get('dni')==dni:
                x=i
                correcto=True
                break
        else: 
            correcto=False
        
        if correcto:
            elimi=datos.pop(x)
            with open("datos.json", "w") as archivo:
                json.dump(datos, archivo)

            print(elimi)
        else: 
            print("Mal")

    """dni=input("dni a Eliminar\n")
    eliminar(dni)"""
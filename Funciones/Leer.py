import json
class Leer():
    def leerDatos(self,dni):
        with open("datos.json", "r") as archivo:
                dato= json.load(archivo)
        if dni==0 or len(dni)==0:
            print("DNI\t Nombre\t Edad\t Ciudad\t Email")
            for d in dato:
                
                print(d['dni'], "\t", d['nombre'], "\t", d['edad'], "\t", d['ciudad'], "\t", d["email"])
        else: 
            x=0
            encontrado=False
            for i, d in enumerate(dato):
                    if d.get('dni')==dni:
                        x=i
                        encontrado=True
                        break
            else:
                encontrado=False
            if encontrado:
                print("DNI\t Nombre\t Edad\t Ciudad\t Email")
                print(dato[x]['dni'], "\t",  dato[x]['nombre'], "\t", dato[x]['edad'], "\t",  dato[x]['ciudad'], "\t",  dato[x]['email'])
            else:
                print("Nif inexistente, volviendo atras...")
                #pintarMenu()
            
    """dni= input("Introduce\n")
    leerDatos(dni)"""

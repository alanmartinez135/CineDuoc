from importlib.util import decode_source
from numpy import column_stack


def crear_pelicula():
    pelicula = []
    titulo = []
    titulo_pelicula = input("Ingresa el titulo de la pelicula: ").capitalize
    titulo.append(titulo_pelicula)
    pelicula.append(titulo)



sala_cine = [["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],
             ["✔","✔","✔","✔","✔","✔","✔","✔","✔","✔"],]


def pelicula():
    print(pelicula, end = ' ')
    for fila in sala_cine:
        for asiento in fila:
            print(asiento, end= ' ')
        print()
    try:
        fila = int(input("Ingresa la fila de tu asiento: "))
        columna = int(input("Ingresa la columna de tu asiento: "))
        if sala_cine [fila][columna] == "✔":
            sala_cine[fila][columna] = '❎'
        else:
            print("Asiento no existe o está ocupado.")
            pelicula()
        for fila in sala_cine:
            for asiento in fila:
                print(asiento, end= ' ')
            print()
    except IndexError:
        print("Datos invalidos")
        pelicula()

def comprar_entradas():
    nombre = input("Ingresa tu nombre: ")
    descuento = 0
    opc = int(input("Eres alumno de DuocUC? \n[1] Sí\n[2] No \n"))
    if opc == 1:
        descuento = 1
        pelicula()
    elif opc ==2:
        descuento = 2
        pelicula()
    else:
        print("Opción Invalida")
        comprar_entradas()

valor_entrada = 2500

def boleta(nombre, descuento):
    print("********************")
    print("*******BOLETA*******")
    print("********************")
    print("PRECIO: $2500")

    
def salir():
    print("Gracias por comprar en Cines DuocUC!")
    exit()


    

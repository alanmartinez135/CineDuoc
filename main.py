import functions as fn

def menu():
    print("Bienvenido a cine DuocUC!\n[1] Comprar Entradas \n[2] Listar entradas \n[3] Salir ")
    opc = int(input("Elige una opción: "))
    if opc == 1:
        fn.crear_pelicula()
        fn.comprar_entradas()
        menu()
    elif opc ==2:
       fn.boleta()
       menu()
    elif opc ==3:
        fn.salir()


menu()   
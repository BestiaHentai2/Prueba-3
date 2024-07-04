import funciones as fn

jugadores = []


while True: 
    print("1.-Registrar puntajes")
    print("2.- listar los puntajes")
    print("3.- imprimir todo tipo")
    print("4.- salir del programa")
    
    op = int(input("ingrese su opcion: "))

    if op == 1:
        fn.registro_puntaje(jugadores)
    elif op == 2:
        fn.listar_puntajes(jugadores)
    elif op == 3:
        fn.imprimir_todo(jugadores)
    elif op == 4:
        print("Saliendo del programa")
        break
    else:
        print("opcion no valida")




#with open()  as archivo
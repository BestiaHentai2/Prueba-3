SHILE =  ["principiante","avanzado","experto"]

JUEGOS = ["fornite","valorant","fifa"]

def registro_puntaje(jugadores):
    ident = input("ingrese identificador del jugador: ")
    nombre = input("nombre y apellido del jugador: ")
    juego1 =  input("ingrese en que primer juego jugo el jugador (Fornite/valorant/fifa): ").lower()
    #juego2 =  input("ingrese en que segundo juego jugo el jugador (Fornite/valorant/fifa): ").lower
    #juego3 = input("ingrese en que tercero juego jugo el jugador (Fornite/valorant/fifa): " ).lower

    #while juego1 not in JUEGOS:
    #    print("Juego no existe")
    #   juego1 = input("ingrese en que primer juego jugo el jugador (Fornite/valorant/fifa): ").lower
    puntaje1 = int(input("ingrese el puntaje1 obtenido  en Fornite: "))
    puntaje2 = int(input("ingrese el puntaje2 obtenido  en valorant: "))
    puntaje3 = int(input("ingrese el puntaje3 obtenido  en fifa: "))
    Tipo = input("que tipo de jugador es (principiante/avanzado/experto): ").lower()
    while Tipo not in SHILE:
        print("El tipo de jugador no entra en ninguna de las categorias")
        Tipo = input("que tipo de jugador es (principiante/avanzado/experto): ").lower()

    jugadores.append(
    {
        "ident" : ident,
        "nombre" : nombre,
        "juego1" : juego1,
        "puntaje1": puntaje1,
        "puntaje2" : puntaje2,
        "puntaje3" : puntaje3,
        "tipo": Tipo,
    })


def listar_puntajes(jugadores):
    print("lista de puntajes")
    for jugador in jugadores:
        print(jugador)    
def imprimir_todo(jugadores):
    jugador_a_imprimir = input("ingrese que categoria desea imprimir (principiante/avanzado/experto): ")
    if jugador_a_imprimir == "":
        jugador_a_imprimir = jugadores
        nombreArchivo = "lista_de_jugadores.txt"
    elif jugador_a_imprimir in SHILE:
        jugador_a_imprimir = []
        for jugador in jugadores:
            if jugador ["tipo"] == jugador_a_imprimir:
                jugador_a_imprimir.append(jugador)
        nombreArchivo = f"jugadores_{jugador_a_imprimir}.txt"
    else:
        print("cargo no valido")
        return
    
    with open(nombreArchivo,"w") as archivo:
        for jugador in jugador_a_imprimir:
            archivo.write(f"ident:{jugador["ident"]}\n")
            archivo.write(f"nombre:{jugador["nombre"]}\n")
            archivo.write(f"juego1:{jugador["juego1"]}\n")
            archivo.write(f"puntaje1:{jugador["puntaje1"]}\n")
            archivo.write(f"puntaje2:{jugador["puntaje2"]}\n")
            archivo.write(f"puntaje3:{jugador["puntaje3"]}\n")
            archivo.write(f"tipo:{jugador["tipo"]}\n")

    
import random
import os
os.system ("cls")
opciones =["piedra", "papel", "tijeras"]

while True: 
    Usuario= input("Elije: piedra, papel o tijeras: ").lower()
    if Usuario not in opciones:
        print("jugada no valida")
        continue

    Pc= random.choice(opciones)
    print(f"La Pc a seleccionado {Pc}")
    print(f"La opcion que elejiste fue {Usuario} ")
    if Usuario == Pc:
        print(f"Empate, los dos eligieron {Usuario}")
    elif Usuario == "piedra" and Pc == "tijeras" :
        print(f"Ganaste, {Usuario} le ganas a {Pc}")
    elif Usuario == "papel" and Pc== "piedra" :
        print(f"Ganaste, {Usuario} le ganas a {Pc}")
    elif Usuario == "tijeras" and Pc == "papel" :
        print(f"Ganaste, {Usuario} le ganas a {Pc}")
    else:
        print(f"perdiste, {Usuario} pierde contra {Pc}")
    

    continuar = input("Desea continuar Si o No: ").lower()
    if continuar == "No".lower() and "N".lower():
        print("Fin del juego")
        break



import random
import os
os.system ("cls")
print("Juego de piedra, papel o tijera.")
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
print("4)Dejar de jugar")

def juego():
      contador=0
      contadorPC=0
      empate=0
      opcion = int(input("Elige una opcion: "))
      Pc = ""
      while opcion !=4:
#Generando el aletatorio del programa de piedra, papel o tijera.
           aleatorio = random.randrange(0,3)
           
#Modulo ramdon y randrage Es una funcion que selecciona al azar de range(start, stop, step).
# de los cuales dos parámetros son opcionales . es decir, start y steps 

#Opciones que el usuario elijira.
           if opcion <0 or opcion >4:
                print("Opcion no valida, por favor intente de nuevo")  
                opcion = int(input("Elige una opcion: "))
           elif opcion == 1:
                Usuario = "Piedra"
           elif opcion == 2:
                Usuario = "Papel"
           elif opcion == 3:
                Usuario = "Tijera"
           elif opcion == 4:
                break
           print(f"La opcion que elejiste fue: {Usuario} ")

#Opciones aletoria de la pc
           if aleatorio == 0:
                Pc = "Piedra"
           elif aleatorio == 1:
                Pc = "Papel"
           elif aleatorio == 2:
                Pc = "Tijera"
           print(f"La opcion que la PC genero aleatoria fue: {Pc}")

#Posibles combinaciones como resultado final
           if  Pc == "Piedra" and Usuario == "Papel":
                print("Ganaste, papel envulve piedra")
                contador+=1
           elif Pc == "Papel" and Usuario == "Tijera":
                print("Ganaste, Tijera corta papel")
                contador+=1
           elif Pc == "Tijera" and Usuario == "Piedra":
                print("Ganaste, Piedra pisa tijera")
                contador+=1
           elif  Pc == "Papel" and Usuario == "Piedra":
                print("Perdiste, papel envulve piedra")
                contadorPC+=1
           elif Pc == "Tijera" and Usuario == "Papel":
                print("Perdiste, Tijera corta papel")
                contadorPC+=1
           elif Pc == "Piedra" and Usuario == "Tijera":
                print("Perdiste, piedra pisa tijera")
                contadorPC+=1
           elif Pc == Usuario:
                print("Empate")
                empate+=1
           opcion=opcion+1
           opcion = int(input("Elige una opcion: "))
           print(f"La compuadora ha ganado {contadorPC} veces")
           print(f"El usuario ha ganado {contador} veces")
           print(f"El juego quedo empate {empate} veces")
           
      
print(juego())

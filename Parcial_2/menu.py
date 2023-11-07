#Importamos todas las funciones del archivo ADN
from ADN import *
print("---------------------------------------------------------------------------------------------------------------------------")
print("Bienvenido al detector de adn")
print("---------------------------------------------------------------------------------------------------------------------------")
print("Tendras que ingresar el ADN para saber si eres mutante o no")
print("---------------------------------------------------------------------------------------------------------------------------")
print("Las unicas letras que se permiten son: A,T,C,G")
print("---------------------------------------------------------------------------------------------------------------------------")
print("Representan cada base nitrogenada del ADN y ademas se guardaran en una matriz de 6x6 que comprobara si eres mutante o no")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
opc = int(input("Ingrese [0] para empezar: "))
counter = 1
#Definimos la variable en donde el se almacenaran los datos de la matriz
matriz = []
num = 0
while opc == 0:
    if counter > 0:
        ADN_MUTANT(matriz)
        sequences = count_sequences(matriz)
        if sequences > 1:
            print("-----------------------------------------")
            print("[ES MUTANTE]")
            print()
            print("SE ENCONTRARON MÁS DE UNA SECUENCIA DE 4 LETRAS IGUALES")
            print("-----------------------------------------")
            counter -= 1
        else:
            print("-----------------------------------------")
            print("[NO ES MUTANTE]")
            print()
            print("NO SE ENCONTRARON SUFICIENTES SECUENCIAS DE 4 LETRAS IGUALES")
            print("-----------------------------------------")
            counter -= 1
    else:
        break

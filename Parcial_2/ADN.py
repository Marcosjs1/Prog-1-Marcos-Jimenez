#Esta funcion es la que crea la matriz
def ADN_MUTANT(matriz):
    # Esta variable es la que define de que tamaño es la matriz
    i = 6
    while i > 0:
        # Se piden los datos por teclado
        data = input("Ingrese las letras del ADN: ").upper()
        print()
        print("-----------------------------------------")
# Estructuras condicionales para verificacion de datos ingresados
        if len(data) != 6:
            print("-----------------------------------------")
            print("NO INGRESO EL NUMERO CORRECTO DE LETRAS")
            print()
            print("POR FAVOR INGRESE LA CANTIDAD CORRECTA")
            print("-----------------------------------------")
        elif validation(data):
            data = list(data)
            matriz.append(data)
            i -= 1
        else:
            print("-----------------------------------------")
            print("INGRESE LAS LETRAS VALIDAS UNICAMENTE")
            print("-----------------------------------------")
    #Bucle para ordenar la matriz
    for row in matriz:
        for element in row:
            print(element, end=" ")
        print()
# Funcion que valida si las letras coinciden con las letras de referencia
def validation(letters):
    valid_dna = ["A", "C", "G", "T"]
    for letter in letters:
        if letter not in valid_dna:
            return False
    return True
#Funcion que verifica si hay secuencias y cuenta la cantidad de estas
def row_horizontal(matriz):
    sequences = 0
# Buccle for que compara el primer valor de la fila con el siguiente
    for row in matriz:
        counter = 1
        previous_letter = row[0]
        for letter in row[1:]:
# Si los tienen el mismo valor se guarda en la variable "counter"
            if letter == previous_letter:
                counter += 1
# Si contador es igual a 4 se a secuencia se le suma 1
                if counter == 4:
                    sequences += 1
                elif counter > 4:
                    sequences -= 1
            else:
                counter = 1
            previous_letter = letter
#Retorna valor de secuencia
    return sequences
#Funcion que verifica si hay secuencia 4 letras iguales y las cuenta
def column_vertical(matriz):
    sequences = 0
#Bucle for para comparar el primer valor de la columna y el primer valor de la fila
    for j in range(len(matriz[0])):
        counter = 1
        previous_letter = matriz[0][j]
        for i in range(1, len(matriz)):
# Si la columna y la fila tienen el mismo valor, se suma uno al contador
            if matriz[i][j] == previous_letter:
                counter += 1
#Si hay mas de 4 coincidencias se suma 1 a secuencias
                if counter == 4:
                    sequences += 1
                elif counter > 4:
                    sequences -= 1
            else:
                counter = 1
            previous_letter = matriz[i][j]
    return sequences
#Funcion que verifica las secuencias de letras en las diagonales de izquierda a derecha y de derecah a izquierda
def diagonal(matriz):
    sequences = 0
#Bucle for en donde se recorre la matriz para buscar las columnas y las filas, comparando los valores diagonales
    for i in range(len(matriz) - 3):
        for j in range(len(matriz[0]) - 3):
#Si se encuentra 4 valores iguales se suma 1 a la secuencia
            if matriz[i][j] == matriz[i + 1][j + 1] == matriz[i + 2][j + 2] == matriz[i + 3][j + 3]:
                sequences += 1
            if matriz[i][j + 3] == matriz[i + 1][j + 2] == matriz[i + 2][j + 1] == matriz[i + 3][j]:
                sequences += 1
    return sequences
#Funcion para sumar las secuencias
def count_sequences(matriz):
    sequences = 0
    sequences += count_horizontal_sequences(matriz)
    sequences += count_vertical_sequences(matriz)
    sequences += count_diagonal_sequences(matriz)
    return sequences

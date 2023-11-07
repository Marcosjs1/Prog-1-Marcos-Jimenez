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

# Funcion que valida si las letras coinciden con las letras de referencia
def validation(letters):
    valid_dna = ["A", "C", "G", "T"]
    for letter in letters:
        if letter not in valid_dna:
            return False
    return True

# Funcion booleana para comprobar si hay 4 letras iguales de manera horizontal
def row_horizontal(matriz):
    for row in matriz:
        counter = 1
        previous_letter = row[0]
        for letter in row[1:]:
            if letter == previous_letter:
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 1
            previous_letter = letter
    return False

# Funcion booleana para comprobar si hay 4 letras de manera horizontal
def column_vertical(matriz):
    for j in range(len(matriz[0])):  
        counter = 1
        previous_letter = matriz[0][j]
        for i in range(1, len(matriz)):
            if matriz[i][j] == previous_letter:
                counter += 1
                if counter == 4:
                    return True
            else:
                counter = 1
            previous_letter = matriz[i][j]
    return False

# Funcion booleana para comprobar si hay 4 letras de manera diagonal
def diagonal(matriz):
# Este bucle for comprueba si hay 4 letras iguales de forma diagonal de izquierda a derecha
    for i in range(len(matriz) - 3):
        for j in range(len(matriz[0]) - 3):
            if matriz[i][j] == matriz[i + 1][j + 1] == matriz[i + 2][j + 2] == matriz[i + 3][j + 3]:
                return True
# Este bucle for comprueba si hay 4 letras iguales de forma diagonal de derecha a izquierda
    for i in range(len(matriz) - 3):
        for j in range(3, len(matriz[0])):
            if matriz[i][j] == matriz[i + 1][j - 1] == matriz[i + 2][j - 2] == matriz[i + 3][j - 3]:
                return True
    return False

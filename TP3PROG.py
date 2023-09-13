# 1-    Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
word = input("Escribe una palabra cualquiera: ")
for i in range(10):
    print("*** ", word, " ***")
# 2- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
# que ha cumplido (desde 1 hasta su edad).
age = int(input("Ingrese su edad: "))
x = age - age + 1
print("Sus años cumplidos son: ")
while x != age:
    print(x)
    x += 1
print(x)
# 3- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
# los números impares desde 1 hasta ese número separados por comas.
num = int(input("Ingrese un numero entero positivo: "))
reply = 0
num_1 = 0
array = ""
while num_1 <= num:
    num_1 += 1
    if (num_1 > 0) and (num_1 % 2 == 0):
        print("")
    else:
        array += str(num_1) + ", "
print(array)
# 4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
# la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Ingrese un número: "))
if num >= 0:
    print("Cuenta atrás:")
    for i in range(num,-1, -1):
        print(i)
else:
    print("Ingrese un número entero positivo")
# 5- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
investment = float(input("Ingrese la cantidad de dinero que desea invertir: $"))
interest = float(input("Ingrese el interés anual: "))
years = int(input("Ingrese la duración de la inversión: "))
total = 0
for n in range(1, years+1):
    profit = ((investment/100)*interest)*n
# 6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como
# el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
num_triangle = int(input("Ingrese un número entero: "))
for i in range(1, num_triangle+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print("")

# 7- Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
mult = 1
while mult < 11:
    print(f"1*{mult}= ", 1*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"2*{mult}= ", 2*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"3*{mult}= ", 3*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"4*{mult}= ", 4*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"4*{mult}= ", 4*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"5*{mult}= ", 5*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"6*{mult}= ", 6*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"7*{mult}= ", 7*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"8*{mult}= ", 8*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"9*{mult}= ", 9*mult)
    mult += 1
mult = 1
while mult < 11:
    print(f"10*{mult}= ", 10*mult)
    mult += 1
# 8_ Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
n = int(input("Ingrese un numero entero positivo: "))
for i in range(1,n+1):
    if (i % 2 != 0):
        for j in range(i, 0 , -1) :
            if (j % 2 != 0):
                print(j,end=" ")
            
    print("")
# 9- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña hasta que introduzca la contraseña correcta.
password = "ProgComB"
pass_input = ""
while pass_input != "ProgComB":
    pass_input = input("Ingrese la contraseña: ")
    if pass_input != "ProgComB":
        print("Contraseña incorrecta.")
print("Contraseña correcta.")
# 10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num = int(input("Ingrese un número entero: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, " no es un número primo")
else:
    print(num, " es un número primo")
# 11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las
# letras de la palabra introducida empezando por la última.
word_input = input("Ingrese una palabra: ")
for i in range(len(word_input)-1, 0-1, -1):
    print(word_input[i])
# 12- Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase = input("Ingrese una frase: ")
letter = input("Ingrese la letra que quiere contar en la frase: ")
phrase = phrase.lower()
letter = letter.lower()
letter_count = phrase.count(letter)
if letter_count == 1:
    print(f"La letra '{letter}' se encuentra {letter_count} vez en la frase '{phrase}'")
elif letter_count > 1:
    print(f"La letra '{letter}' se encuentra {letter_count} veces en la frase '{phrase}'")
else:
    print(f"La letra '{letter}' no se encuentra en la frase '{phrase}'")
# 13_Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
i = 0
while i == 0:
    word = input("Escriba algo: ")
    print (f"[{word}]")
    if (word == "salir") or (word == "Salir"):
        break
# 14_Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
if (num_1 % 2 == 0):
    print(f"{num_1} es PAR")
else:
    print(f"{num_1} es IMPAR")
if (num_2 % 2 == 0):
    print(f"{num_2} es PAR")
elif (num_2 != 0):  
    print(f"{num_2} es IMPAR")
# 15- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num = int(input("Ingrese un número entero mayor a 0:"))
div = 1
for i in range(num):
    if num % div == 0:
        print(f"{div} es divisor de {num}")
    div += 1
# 16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba
# cuántos negativos ha introducido.
num_amount = int(input("¿Cúantos números va a ingresar? "))
n = 1
negative_nums = 0
while n < num_amount+1:
    num = int(input("Ingrese un número: "))
    if num < 0:
        negative_nums += 1
    n += 1
print(f"Ha ingresado {negative_nums} números negativos")
# 17- Solicitar al usuario que ingrese una frase y luego imprimir un
# listado de las vocales que aparecen en esa frase (sin repetirlas).
phrase_1 = input("Ingrse una frase: ")
print("Lista de vocales encontradas en la frase: ", phrase_1)
phrase_1 = phrase_1.lower()
if phrase_1.find("a") >= 1:
    print("a")
if phrase_1.find("e") >= 1:
    print("e")
if phrase_1.find("i") >= 1:
    print("i")
if phrase_1.find("o") >= 1:
    print("o")
if phrase_1.find("u") >= 1:
    print("u")
# 18_Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
fib = int(0)
fib_2 = int(1)
result = int(0)
while result < 55:
    for i in range (0, 10-1):
        result = (fib) + (fib_2)
        fib =  fib_2
        fib_2 = result
        print(result)
# 19- Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad,
# que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y
# otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
# El programa deberá comprobar que las cantidades ingresadas sean positivas.
goal = int(input("¿Cúanto dinero desea ahorrar? $"))
saved = 0
while saved < goal:
    saving = 0
    saving = int(input("Ingrese la cantidad que desea ahorrar hoy: $"))
    saved += saving
    print(f"Has ingresado {saving}. Te faltan ${goal - saved}")
if saved >= goal:
    print(f"Felicidades, has alcanzado tu meta de {goal}. Cantidad ahorrada: {saved}")
# 20_Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
num = int(input("Ingrese un numero entero: "))
sum = 0
while sum != 0:
    sum += num
    num = int(input("Ingrese otro numero para sumar o 0 si desea salir: "))
print(f"La suma total es {sum}")
# 21- Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
# Informar cuál fue el mayor número ingresado.
num = int(input("Ingrese un número entero: "))
biggest = num
while num != 0:
    num = int(input("Ingrese otro número o ingrese 0 para salir: "))
    if num > biggest:
        biggest = num
print("El número ingresado más grande es: ", biggest)
# 22- Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los
# dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar
# cuántos de los números ingresados por el usuario fueron números pares.
nums = 0
digits_sum = 0
pair = 0
while nums != "-1":
    nums = input("Ingrese un número: ")
    if nums == "-1":
        break
    for x in nums:
        if x == "-":
            continue
        else:
            digits_sum += int(x)
    print("La suma de los dígitos del número ingresado es: ", digits_sum)
    print("Para terminar ingrese el número -1.")
    if int(nums) % 2 == 0:
            pair += 1
    digits_sum = 0
print(pair, " de los números ingresados fueron números pares.")

# 23_ Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
cost = int(0)
while True:
    mount = int(input("Ingrese el monto del producto: "))
    cost = cost + mount
    if mount == 0:
        break
print(f"El costo total es de: $ {cost}")
# 24_Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento
print("Bienvenido al sistema")
mount = 1
total = 0
end_loop = 1
while end_loop != 0:
    mount = int(input("Ingrese el monto a pagar por su producto: $"))
    if mount < 0:
        print("Por favor, ingrese un monto válido")
        continue
    elif mount == 0:
        print("El total final a pagar es de: $", total)
        end_loop = 0
        break
    else:
        total += mount
    print("Total a pagar: $", total)
if total > 1000:
    total = total - (total * 0.10)
    print("Por exeder los $1000 obtienes un descuento del 10%. El total final a pagar es de: $", total)
# 25_Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1
num = int(input("Ingrese el numero que desea saber el factorial: "))
cont = num
numero = num
for i in range(num-1):
    cont = cont - 1
    fact = (num * cont)
    num = fact
    print(numero, "*", cont, " = ", fact)
print(f"El factorial de {numero} es {fact}")

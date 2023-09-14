# 1_Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
años = int(input("Ingrese los años de antiguedad de la computadora: "))
print("")
if (años <= 2) and (años > 0):
    print("La computadora es nueva")
elif (años > 2):
    print("La computadora es vieja")
# 2_Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
años = int(input("Ingrese los años de antiguedad de la computadora: "))
print("")
if (años <= 2) and (años > 0):
    print("La computadora es nueva")
elif (años > 2):
    print("La computadora es vieja")
elif (años < 0):
    print("ERROR")
# 3_Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.
nom_1 = input("Ingrese el nombre: ")
nom_2 = input("Ingrese el nombre: ")
letra_1 = nom_1[0].lower()
letra_2 = nom_2[0].lower()
if (letra_1 == letra_2):
    print("Las letras coinciden")
else:
    print("Las letras no coinciden")
# 4_Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.
print("Bienvenido al sistema")
print("Ingrese [1-(Para el Partido Rojo)] - [2-(Para el Partido Verde)] - [3-(Para el Partido Azul)]")
voto = int(input("Ingrese el numero del partido que quiera elegir: "))
if (voto == 1):
    print("Usted eligio el Partido Rojo ")
elif (voto == 2):
    print("Usted eligio el Partido Verde")
elif (voto == 3):
    print("Usted eligio el Partido Azul")
elif (voto > 3):
    print("ERROR")
# 5_Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato
letra = input("Ingrese una letra: ")
if len(letra) >= 2:
    print("Solo debe ingresar una letra")
    exit()
elif letra.upper() == "A":
    print("Es una vocal")
elif letra.upper() == "E":
    print("Es una vocal")
elif letra.upper() == "I":
    print("Es una vocal")
elif letra.upper() == "O":
    print("Es una vocal")
elif letra.upper() == "U":
    print("Es una vocal")
else:
    print(letra, " Es una consonante")
#6_Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

bis = int(input("Ingrese un año: "))
if (bis < 100) and (bis > 0):
    if (bis % 4 == 0):
        print("El año ",bis, " es año bisiesto")
elif (bis >= 100) and ( bis < 400):
    if (bis % 4 == 0) and (bid % 100 != 0):
        print("El año ",bis, " es año bisiesto")
elif (bis >= 400 ):
    if (bis % 4 == 0) and (bis % 100 != 0) and (bis % 400 != 0):
        print("El año ",bis, " es año bisiesto")
# 7_Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
nums = input("Ingrese 3 numeros [x , y , z]: ")
nums = nums.split()
num1 = nums[0]
num2 = nums[1]
num3 = float(nums[2])
num1 = float(num1[0:num1.find(",")])
num2 = float(num2[0:num2.find(",")])
menor = num1
if (menor > num2):
    menor = num2
elif (menor > num3):
    menor = num3
print("El menor de los numeros es ",menor)
# 8_Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”
usuario = input("Ingrese le nombre de usuario: ")
contr = input("Ingrese la contraseña: ")
if (usuario == "Gwenevere") and (contr == "excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")
# 9_Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("Ingrese su nombre: ")
nombre = nombre.capitalize()
genero = input("Ingrese su sexo (M/F): ")
genero = genero.capitalize()
if nombre[0] == ("A" or "a" or "B" or "b" or "C" or "c" or "D" or "d" or "E" or "e" or "F" or "f" or "G" or "g" or "H" or "h" or "I" or "i" or "J" or "j" or "K" or "k" or "L" or "l") and (genero   == "F" or "f"):
    print("Pertenece al grupo A")
elif nombre[0] == ("O" or "o" or "P" or "p" or "Q" or "q" or "R" or "r" or "S" or "s" or "T" or "t" or "U" or "u" or "V" or "v" or "W" or "w" or "X" or "x" or "Y" or "y" or "Z" or "z" ) and (genero == "M" or "m"):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")
# 10_Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.
print("Bienvenido a Arcade")
edad = int(input("Para ingresar primero dinos tu edad: "))
if (edad < 4):
    print("Puede ingresar sin costo")
elif (edad >=4) and (edad <= 18):
    print("El costo para ingresar es de $500")
elif (edad > 18):
    print("El costo para ingresar es de $1000")
# 11_ La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
vegetariano  =  False
print("BIENVENIDO a la toma de pedido de la pizzeria Bella Napoli")
print("A continuacion, indique si prefiere un menu vegetariano o no vegetariano")
input("(si) para menu vegetariano. (no) para un menu no vegetariano" )
vegetariano = input()
print("Todas las pizzas llevan tomate y mozzarella. A continuacion elija los ingredientes extra: ")
if (vegetariano ==  True):
    print("Escriba el ingrediente seguido de una coma, un espacio y el siguiente ingrediente asi: ")
    print("ingrediente, ingrediente, ingrediente")
    print("Ingredientes vegetarianos: ")
    print("")
    print(" -Pimiento")
    print(" -Tofu")
    ingrediente = input()
elif (vegetariano == False): 
    print("Escriba el ingrediente seguido de una coma, un espacio y el siguiente ingrediente asi: ")
    print("ingrediente, ingrediente, ingrediente")
    print("Ingredientes vegetarianos: ")
    print("")
    print(" -Pepperoni")
    print(" -Jamon")
    print(" -Salmon")
    ingrediente = input()

if vegetariano == True:
    print("Pizza vegetariana. Ingredientes: ")
    print(ingrediente)

# 12_Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

years = input("Ingrese el año actual y un año cualquiera [año_actual, año_x]: ")
an_actual = int(years[0:years.find(",")])
an_x = int(years[years.find(" ")+1:])
if an_actual > an_x:
    pas = (an_actual - an_x)
    print(f"Han pasado {pas} años desde el año {an_x}")
if an_actual < an_x:
    falt = (an_x - an_actual)
    print(f"Faltan {falt} años para el el año {an_x}")
# 13_Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
if numero1 <= 0 or numero2 <= 0:
    print("Por favor, ingrese valores positivos y diferentes de cero.")
else:
    if numero1 > numero2:
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1
    if mayor % menor == 0:
        print(f"{mayor} es múltiplo de {menor}.")
    else:
        print(f"{mayor} no es múltiplo de {menor}.")
# 14_Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
# x = -b / a
print("Ecuacion a resolver: a x + b = 0")
valor_a = int(input("Ingrese el valor de a: "))
valor_b= int(input("Ingrese el valor de b: "))
if (valor_a == 0) or (valor_b == 0):
    print("Error")
else:
    valor_x = -valor_b / valor_a
    print(f"El valor de x es: {valor_x}")
# 15_Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
preg =input("¿Que desea calcular? Si desea calcular el area de un triangulo ingrese [T o t] y si desea calcular el area de un circulo ingrese [C o c]: ")
if preg.upper() == "T":
    b = float(input("Ingrese la base del triangulo: "))
    h = float(input("Ingrese la altura del triangulo: "))
    area = (b * h) / 2
elif preg.upper() == "C":
    r = float(input("Ingrese el radio del circulo: "))
    import math
    area = (math.pi * r**2)
    print(f"El area del circulo  es {area}")
else:
    print("Error")
# 16_Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#Si operación es 1 entonces debemos ver el resultado de a + b
#Si operación es 2 entonces debemos ver el resultado de a * b
#Si operación es 3 entonces debemos ver el resultado de a - b
#Si operación es 4 entonces debemos ver el resultado de a / b
print("Ingrese 2 valores")
a = int(input())
b = int(input())

print("Elija que operacion realizara: [Suma,resta,division,multiplicacion]")
print("Al restar, se hara (a-b) y al dividir se hara (a/b)")
print("Escribir el nombre de una de ellas sin comas, ni espacios y ni mayusculas: ")
op = input()

if op == "suma":
    resultado = a+b
    print(f"El resultado es {resultado}")
elif op == "resta":
    resultado = a-b
    print(f"El resultado es {resultado}")
elif op == "multiplicacion":
    resultado = a*b
    print(f"El resultado es {resultado}")
elif op == "division":
    if (a == 0 or b == 0):
        print("Error")
    else:
        resultado = a/b
        print(f"El resultado es {resultado}")

# 17_Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia = input("¿Que dia de la seman es hoy?")
dia = dia.lower()
if dia == "lunes":
    print(f"Hoy es {dia} ¡Feliz inicio de semana!")
elif dia == "viernes":
    print(f"Hoy es {dia} ¡Feliz fin de semana!")
elif dia == "martes" or dia == "miercoles" or dia == "jueves":
    print(f"Hoy es {dia} ¡A seguir trabajando!")
elif dia == "sabado" or dia == "domingo":
    print(f"Hoy es{dia} ¡A descansar!")
# 18_Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))
jornada_minima = 48.0
if horas_trabajadas > jornada_minima:
    horas_extras = horas_trabajadas - jornada_minima
else:
    horas_extras = 0.0

salario_total = (jornada_minima * salario_por_hora) + (horas_extras * salario_por_hora * 1.10)
print(f"Horas extras trabajadas: {horas_extras} horas")
print(f"Salario total: ${salario_total:.2f}")
# 19_Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
cantidad = int(input("Ingrese la cantidad de lapices que desea comprar: "))
if cantidad >= 1000:
    total = (cantidad * 60 ) * 0.93
    print(f"El total final a pagar con un descuento del 7% sera de: $ {total}")
else:
    print("El total a pagar sera de: $," (cantidad * 60))
# 20_ Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("Ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))
nota_4 = float(input("Ingrese la nota 4: "))

prom = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if prom >= 6 :
    print(f"Felicidades, su promedio es de {prom}, usted aprobo")
else:
    print(f"Usted ha desaprobado con un promedio de {prom}")

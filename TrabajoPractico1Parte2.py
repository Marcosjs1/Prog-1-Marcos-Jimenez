"""Ejercicio 1"""
base = float(input("Ingrese la medida de la base del rectangulo: "))
altura = float(input("Ingrese la medida de la altura del rectangulo: "))
area = (base*altura)
perimetro = (base*2) + (altura*2)
print("El area del rectangulo es: ",area)
print("El preimetro del rectangulo es: ",perimetro)

"""Ejercicio numero 2"""
cateto_1 = int(input("Ingrese el cateto 1: "))
cateto_2 = int(input("Ingrese el cateto 2: "))
hipotenusa = (cateto_1**2) + (cateto_2**2)
hipotenusa1 = hipotenusa**0.5
print("El valor de la hipotenusa es: ", float(hipotenusa1))

"""Ejercicio 3"""
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
suma = (num_1 + num_2)
resta = (num_1 - num_2)
div = (num_1 / num_2)
mult = (num_1 * num_2)
print("La suma entre los 2 numeros da como resultado: ",suma)
print("La resta entre los 2 numeros da como resultado: ", resta)
print("La division entre los 2 numeros da como resultado: ",div)
print("La multiplicaion entre los 2 numeros da como resultado: ",mult)

"""Ejercicio 4"""
Far = float(input("Ingrese temperatura en grados Farenheit: "))
Cel = (Far-32) * 5 / 9
print(f"La temperatura en grados Celsius es de: {Cel}°")

"""Ejercicio 5"""
# a) A = input(nombre, ¿cual es tu cancion favorita?)
#   El problema es que se quisieron concatenar 2 elementos dentro del input
# Para solucionarlo es asi:
    print(nombre,"¿cual es tu cancion favorita?")
# b) precio = input("Precio: ")
#   total = precio +(precio * 0.1)
#   En este ejemplo, "precio" esta guardando una cadena de texto y luego se esta queriendo multplicar, lo correcto seria:   
    precio = int(input("Precio: "))
    total = precio + (precio*0.1)  
# c) edad = int(input(“Edad: “))
#   print(tu edad es, edad)
# El problema del ejemplo es que se esta asignando el valor "18" a una variable dentro de un print(), lo correcto, para comprobar si "edad" es igual a "18", seria lo siguiente:
    edad = int(input("Edad: "))
    print("Veamos si tu edad es 18...")
    if edad == 18:
        print("Tu edad es 18")
    else:
        print("Tu edad no es 18")

"""Ejercicio 6"""
num_1 = int(input("Ingresa el primer numero: "))
num_2 = int(input("Ingresa el segundo numero:"))
num_3 = int(input("Ingresa le tercer numero: "))
media = (num_1 + num_2 + num_3) / 3
print (f"La media de los 3 numeros es: {media}")

"""Ejercicio numero 7"""
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = int(minutos/60)
horas1 = minutos % 60
print (horas,"hs",horas1,"minutos")

"""Ejercicio 8"""
sueldo_b = int(25000)
venta_1 = float(input("Ingrese la ganancia de la primer venta: "))
venta_2 = float(input("Ingrese la ganancia de la segunda venta: "))
venta_3 = float(input("Ingrese la ganancia de la tercer venta: "))
extra_1 = (venta_1 / 10)
extra_2 = (venta_2 / 10)
extra_3 = (venta_3 / 10)
sueldo_f = (sueldo_b + (extra_1 + extra_2 + extra_3))
print(f"El sueldo final de la persona es: {sueldo_f}")

"""Ejercicio 9"""
precio = float(input("Ingrese el costo de lo que compro: "))
descuento = (precio * 0.15)
precio_final = (precio - descuento)
print(f"El precio final de su compra es: {precio_final}$")

"""Ejercicio 10"""
parcial_1 = float(input("Ingrese la nota del parcia 1: "))
parcial_2 = float(input("Ingrese la nota del parcia 2: "))
parcial_3 = float(input("Ingrese la nota del parcia 3: "))
examen_final = float(input("Ingrese la nota del examen final: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))
promedio_parcial = (parcial_1 + parcial_2 + parcial_3) / 3
nota_final = (promedio_parcial * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"La calificacion final del alumno es: {nota_final}")

"""Ejercicio 11"""
num_1 = int(input("Ingresa el primer numero: "))
num_2 = int(input("Ingresa el segundo numero: "))
dist = abs(num_1 - num_2)
print(f"La distancia entre los numeros es de: {dist}")

"""Ejercicio 12"""
num = int(input("Ingrese el numero: "))
r_cuadrada = (num ** (1/2))
r_cubica = (num ** (1/3))
print(f"La raiz cuadrada de {num} es: {r_cuadrada} y la raiz cubica de {num} es: {r_cubica}")

"""Ejercicio 13"""
num = input("Ingrese un numero de 2 cifras: ")
print(num[::-1])

"""Ejercicio 14"""
A = int(input("Ingrese un numero: "))
B = int(input("Ingrese un numero: "))
print(f"El valor de A es: {A} y el valor de B es: {B}")
A = B
B = A
print(f"Ahora el valor de A es: {A} y el valor de B es: {B}")

"""Ejercicio 15"""
HH = 20
MM = 47
SS = 24
print(f"Hora de salida: [{HH}:{MM}:{SS}]")
T = 10800
SS = T + SS
if SS > 59:
    MM = MM + (SS/60)
    SS = (SS % 60)
if MM > 59:
    HH = int(HH + (MM/60))
    MM = int((MM % 60))
if HH > 24:
    HH = 0
print (f"Hora de llegada: [{HH}:{MM}:{SS}]")        

"""Ejercicio 16"""
nom = input("Ingrese el nombre: ")
ap = input("Ingrese el apellido 1: ")
ap_2 = input("Ingrese el apellido 2: ")
print(nom[0],".",ap[0],".",ap_2[0])

"""Ejercicio 17"""
usuario = input("Ingrese su nombre: ")
print("Ahora estas en la Matrix",usuario)

"""Ejercicio 18"""
costo = float(input("Ingrese el costo de la comida: "))
serv = (costo * 0.062)
prop = (costo * 0.10)
costo_final = (costo + serv + prop)
print(f"El precio final de la comida es de: {costo_final}")

"""Ejercicio 19"""
dia = int(input("Ingrese el dia de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
año = int(input("Ingrese el año de su nacimiento: "))
print(dia,"/",mes,"/",año)

"""Ejercicio 20"""
fecha = [input("Ingrese el dia de nacimiento: "),input("Ingrese el mes de nacimiento: "),input("Ingrese el año de nacimiento: ")]
print(fecha)

"""Ejercicio 21"""
recorrido = float(input("Indique la cantida KM que tiene que recorrer: "))
consumo = (recorrido * 0.04)
combustible = int(20)
gasto = (consumo/combustible)
gasto_km = 4 * 100
recorrido = (combustible / gasto_km) 
print(f"La capacidad del tanque es de: {combustible}lts")
print("El gasto de de combustible por cada 100km es de 4 lts")
print(f"Usted puede recorrer {gasto_km}KM sin necesidad de cargar combustible")
if consumo > combustible:
    print("La cantidad de combustible no es suficiente tiene que cargar")
    print(f"El consumo es de: {consumo}lts, usted tiene que recargar: {gasto} tanques")
else:
    print("La cantidad de cobustible es sufieciente, puede viajar tranquilamente")

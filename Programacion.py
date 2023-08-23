""" Ejercicio parte 1"""
dia =  input("Ingrese dia de la semana: ")
if (dia == "Lunes") or (dia == "lunes"):
    print("Nivel inicial")
elif (dia == "Martes") or ( dia == "martes"):
    print("Nivel intermedio")
elif (dia == "Miercoles") or (dia == "miercoles"):
    print("Nivel avanzado")
elif (dia == "Jueves") or (dia == "jueves"):
    print("Practica hablada")
elif (dia == "Viernes") or (dia == "jueves"):
    print("Ingles para viajeros")
"""Ejercicio parte 2"""
dia_solicitado = input("Ingrese el dia,[DD/MM]: ")
sem = (dia_solicitado[0:dia_solicitado.find(",")])
num = (dia_solicitado[dia_solicitado.find(" "): dia_solicitado.find("/")])
num = int(num)
mes = (dia_solicitado[dia_solicitado.find("/")+1])
mes = int(mes)
if (sem == "Lunes") or (sem == "lunes") or (sem == "Martes") or (sem == "martes") or (sem == "Miercoles") or (sem == "miercoles") or (sem == "Jueves") or (sem == "jueves") or (sem == "Viernes") or (sem == "viernes"):
    if (num <= 31):
        if (mes <=12):
            print("")
else:
    exit()
"""Ejercicio parte 3"""
exam = input("Indica si el dia ingresado hubo examen: ")
if (exam == "Si") or (exam == "si"):
    if (sem == "Lunes") or (sem == "lunes") or (sem == "Martes") or (sem == "martes") or (sem == "Miercoles") or (sem == "miercoles"):
        aprob = int(input("Cuantos alumnos aprobaron: "))
        desaprob = int(input("Cuantos alumnos desaprobaron: "))
        porc = (aprob + desaprob) * (aprob/100)
        print(porc)
else: 
    if (sem == "Jueves") or (sem == "jueves"):
        asist = int(input("Indique su porcentaje de asistencia: "))
        if (asist >= 50):
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    else:
        if ((num == 1) and (mes == 1)) or ((num == 1) and (mes == 7)):
            print("Comienzo de nuevo ciclo")
            ciclo = int(input("Ingrese la cantidad de alumnos: "))
            p = int(input("Indique el arancel por alumno: "))
            ing_total = (ciclo) * (p)
            print(ing_total,"$")


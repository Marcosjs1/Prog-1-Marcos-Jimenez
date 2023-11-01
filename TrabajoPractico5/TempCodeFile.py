from TrabajoPractico5 import id_club, is_multiple_of, average_temperature, extra_space, min_max_num, area_perimeter_circumference, login, list_reciever, is_prime_num, factorial, digit_in_number, digit_sum
biggest_num = 0
num = ""
while num != " ":
    num = input("Ingrese un número primo (para finalizar ingrese un número no primo): ")
    if is_prime_num(int(num)) != False:
        digit = input("Ingrese el dígito que desea buscar en el número ingresado: ")
        print(f"La suma de los dígitos del número {num} es: {digit_sum(num)}")
        print(f"El digito '{digit}' se repite {digit_in_number(num, digit)} veces en el número '{num}'")
        if int(num) > biggest_num:
            biggest_num = int(num)
    else:
        break
print(biggest_num)
print(f"El factorial del mayor número ingresado ({biggest_num}) es: {factorial(biggest_num)}")
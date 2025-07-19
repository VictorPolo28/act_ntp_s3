#Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.


suma_total = 0

while  True:
    number = input("Ingrese un numero diferente de  Cero (Ingrese 0 para salir): ")
    if number == "0":
        break
    suma_total += float(number)

print("la suma total es: ", suma_total)
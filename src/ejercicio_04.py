

suma_total = 0

while  True:
    number = input("Ingrese un numero diferente de  Cero (Ingrese 0 para salir): ")
    if number == "0":
        break
    suma_total += float(number)

print("la suma total es: ", suma_total)
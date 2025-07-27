#Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.

numero = input("un número entero positivo: ")
resultado = 0


for suma in numero:
     resultado += int(suma)
print(resultado)
#Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas) hay en la frase frase = "programacion es divertida" y muestra el total.

frase  = "programacion es divertida".lower()
vocales ="aeiou"
cantidad_de_vocales = 0
for letras in frase :
    if letras in vocales:
        cantidad_de_vocales += 1
print("la caitd de vocales es: ",cantidad_de_vocales )
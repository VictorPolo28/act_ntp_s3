   
palabras_escritas = 0
while True :
    palabra = input("Ingrese una palabra cualquiera: ")
    if palabra == "fin":
        break
    palabras_escritas += 1

print("Se ingresaron", palabras_escritas, " palabras")
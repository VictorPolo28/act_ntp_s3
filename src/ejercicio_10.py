#Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. Al final, muestra cuántas palabras se leyeron (sin contar “fin”).
   
palabras_escritas = 0
while True :
    palabra = input("Ingrese una palabra cualquiera: ")
    if palabra == "fin":
        break
    palabras_escritas += 1

print("Se ingresaron", palabras_escritas, " palabras")
#Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.
import random


while True:
    numero_random = random.randint(1,10)
    numero =int(input(" Ingre un numero del 1 al 10: "))
    if numero_random  == numero:
        break
    else : 
        print("Intenta de nuevo ")
print("Felicidadeshas adivinado el numero: ", numero)
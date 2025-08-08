import random


while True:
    numero_random = random.randint(1,10)
    numero =int(input(" Ingre un numero del 1 al 10: "))
    if numero_random  == numero:
        break
    else : 
        print("Intenta de nuevo ")
print("Felicidadeshas adivinado el numero: ", numero)
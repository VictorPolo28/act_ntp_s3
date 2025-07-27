#Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea.

import time


minut = 0
second = 0

while second < 60:
    print(f'{minut:02}:{second:02}')
    time.sleep(1)
    second += 1
 
#Mediante un ciclo while, genera y muestra la secuencia de Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.

number_1, number_2 = 0, 1

while number_1 <= 1000:
    print(number_1, end=" ")
    number_1, number_2 = number_2, number_1 + number_2
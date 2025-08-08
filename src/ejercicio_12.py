factorial = 1
multiplos = 1
numero = int(input  ("Ingrese un nomero entero"))
    
while multiplos <= numero:
    factorial *= multiplos
    multiplos += 1
    
print("El numero  facturia   de ",numero, " es :", factorial)
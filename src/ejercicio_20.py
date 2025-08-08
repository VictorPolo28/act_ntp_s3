

edades = []
edad = 0
while edad != -1:
    edad = int(input("Ingrese  una edad  o -1 para salir: "))
    if  edad >=100 :
        print("No esposible agregar   una edad tan vieja")
    elif edad != -1:
        edades.append(edad)
    
edades.sort()
print(f'Le edad mayor ingresada es : ',edades[-1])
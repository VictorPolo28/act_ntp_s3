fruta = "manzana".lower()
vocal ="a"
numero_de_a = 0
for letras in fruta:
    if letras in vocal:
        numero_de_a += 1
    
print(numero_de_a)
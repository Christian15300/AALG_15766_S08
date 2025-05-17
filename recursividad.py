def sumaresta(lista, x=0):
    if x == len(lista):
        return 0

    n = lista[x]

    if (n // 2) * 2 == n:  
        return n + sumaresta(lista, x + 1)
    else:  
        return -n + sumaresta(lista, x + 1)

lista = [2, 3, 8, 1]
z = sumaresta(lista)
print(z)  

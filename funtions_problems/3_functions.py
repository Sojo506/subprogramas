"""
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
"""

numeros_pares = [2,4,6,8,10,12,14,16,18,20]


def aplicar_funcion(funcion, lista):
    numeros_impares = []
    for i in lista:
        numeros_impares.append(convertidor_impares(i))
    return numeros_impares

def convertidor_impares(n):
    return n + 1

print()
print(aplicar_funcion(convertidor_impares,[2,4,6,8,10,12,14,16,18,20]))
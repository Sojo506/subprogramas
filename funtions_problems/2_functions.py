"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""

import math as ma

# Funciones para el menu


def lineaSup(largo):
    linea = "   ╔"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╗"
    print(linea)


def lineaMed(largo):
    linea = "   ╠"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╣"
    print(linea)


def lineaInf(largo):
    linea = "   ╚"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╝" + "\n"
    print(linea)


def lineaBlanco(largo):
    linea = "   ║"
    for i in range(1, largo-1):
        linea += " "
    linea += "║"
    print(linea)


def lineaDato(d, largo):
    linea = ""
    linea += "   ║ "
    linea += d
    blancos = largo - len(d)
    for i in range(1, blancos-2):
        linea += " "
    linea += "║"
    print(linea)


def menuPrincipal():
    lineaSup(60)
    lineaBlanco(60)
    lineaDato("                  Calculadora científica", 60)
    lineaBlanco(60)
    lineaMed(60)
    lineaBlanco(60)
    lineaDato("01. Calcular el Seno ", 60)
    lineaDato("02. Calcular el Coseno", 60)
    lineaDato("03. Calcular la Tangente", 60)
    lineaDato("04. Calcular el Exponencial", 60)
    lineaDato("05. Calcular el logaritmo neperiano", 60)
    lineaDato("06. Salir", 60)
    lineaBlanco(60)
    lineaInf(60)


# Funcion para calcular el seno
def seno(x):
    print("\t.:Resultados:.")
    print()
    for s in range(1,x+1):
        print(f"Seno de {s}: {ma.sin(s):.2f}")

    print()
    return 'Listo!'


# Funcion para calcualr el coseno
def coseno(x):
    print("\t.:Resultados:.")
    print()
    for c in range(1,x+1):
        print(f"Coseno de {c}: {ma.cos(c):.2f}")

    print()
    return 'Listo!'


# Función para calcular la tangente
def tangente(x):
    for t in range(1, x+1):
        print(f"Tangente de {t}: {ma.tan(t):.2f}")

    return "Listo!"


# Función para calcular el exponencial
def exponencial(x):
    print("\t.:Resultados:.")
    print()
    for e in range(1, x+1):
        print(f"Exponencial de {e}: {ma.exp(e):.2f}")

    print()
    return 'Listo!'
    


# Función para calcular el logaritmo neperiano
def neperiano(x):
    print("\t.:Resultados:.")
    print()
    for n in range(1, x):
        print(f"Logaritmo de {n}: {ma.log(n):.2f}")

    print()
    return 'Listo!'


while True:
    menuPrincipal()
    print()
    while True:
        try:
            opc = int(input("   Favor ingresar su opción: "))
            break
        except ValueError:
            print("Valor incorrecto!")

    if opc == 1:
        while True:
            try:
                valor = int(input("Ingresa un valor entero -> "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print(seno(valor))
        print()
    elif opc == 2:
        while True:
            try:
                valor = int(input("Ingresa un valor entero -> "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print(coseno(valor))
        print()
    elif opc == 3:
        while True:
            try:
                valor = int(input("Ingresa un valor entero -> "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print(tangente(valor))
        print()
    elif opc == 4:
        while True:
            try:
                valor = int(input("Ingresa un valor entero -> "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print(exponencial(valor))
        print()
    elif opc == 5:
        while True:
            try:
                valor = int(input("Ingresa un valor entero -> "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print(neperiano(valor))
        print()
    elif opc == 6:
        print('You got it!')
        break

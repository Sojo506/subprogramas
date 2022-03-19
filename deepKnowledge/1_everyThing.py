import sys #para el primer ejercicio

import datetime #para el segundo ejercicio

import math #para el tercer ejercicio

while True:
    print("""\nDigite algún ejercicio del (1) al (5)
Exit: (6)
""")
    opc = int(input("Ejercicio -> "))

    #Obtener la versión actual de python
    if opc == 1:
        print(f"\n\tVersión de Python: {sys.version}")
        print(f"Información de versión: {sys.version_info}")

    #Mostrar en pantalla la fecha y hora actuales del sistema        
    elif opc == 2:
        ahora = datetime.datetime.now()
        print(f"\nFecha y hora actuales: {ahora}")
        print(type(ahora))
        print()
        # fecha con formato
        ahora_format = ahora.strftime("%H:%M:%S %Y-%m/%d")
        print(ahora_format)

    #Solicitar al usuario el radio de un círculo y calcular su área
    elif opc == 3:
        radio = float(input("Digite el radio de un círculo -> "))
        area = math.pi * radio**2
        print(f"Su área es: {area:.2f}")

    #Pedir nombre al usuario y mostrarlo de forma inversa
    elif opc == 4:
        nombre = input("Digite tu nombre -> ")
        print(f"Tu nombre invertido: {nombre[::-1]}")

    #Calcular el área de un triángulo dadas la base y la altura
    elif opc == 5:
        base = float(input("\nDigite la base del triángulo: "))
        altura = float(input("Y digite la altura: "))
        ope = base * altura /2
        print(f"El área de tu triángulo es: {ope}")

    elif opc == 6:
        print("You can do it better!")
        break

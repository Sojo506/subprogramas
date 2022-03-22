"""
    Desarrolle un programa que le solicite al usuario
    dos números, con estos valores debe mostrar el
    resultado de la suma, la resta, la multiplicación y
    la división.
"""
#Funciones ejercicio 1

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a//b



"""
    Desarrolle un programa que lea la
    cédula de un funcionario, su nombre y
    su salario bruto. Posteriormente, debe
    calcular el 8% de la CCSS, el 1% del
    Banco Popular, el total de deducciones
    y el salario neto. Al final debe imprimir
    la información como se muestra a la
    derecha.
"""

#Funciones ejercicio 2
def ccss(salario):
    return salario * 8 // 100

def banco(salario):
    return salario * 1 // 100

def total_deducciones(salario):
    return banco(salario) + ccss(salario)

def salario_neto(salario):
    return salario - total_deducciones(salario)



"""
Desarrolle un programa que le solicite al usuario
el lado de un cuadrado, con esta información
debe mostrarle su área y su perímetro.
"""

#Funciones ejercicio 3

def area(lado):
    return lado * lado

def peri(lado):
    return lado * 4


"""
Desarrolle un programa que lea dos valores
numéricos y que muestre el resultado de elevar
el primer valor a la potencia del segundo valor.
"""

#Funciones ejercicio 4

def elevar(a,b):
    return a**b



"""
Desarrolle un programa que lea el precio unitario
de un producto, la cantidad que se desea
comprar, a partir de esta información debe
calcular el precio final a pagar, considere que
debe aplicarle un 10% de descuento y el IVA.
"""

#Funciones ejercicio 5

def descuento(t):
    return t * 10 // 100

def impuesto(t):
    return t * 13 // 100


"""
Desarrolle un programa que le solicite al usuario un número y
le muestre cuál es el correspondiente número en base binaria,
octal y hexadecimal.
Cada una de las bases debe ser un proceso independiente.
El proceso binario debe mostrar el resultado, los otros dos
procesos deben retornar el resultado para ser mostrado desde
el proceso inicial.
Adicionalmente, programe un proceso que reciba dos
parámetros (el valor y la base) y que muestre el número
correspondiente.
"""

#Funciones ejercicio 6

def decimal_binario(x):
    binario = []
    while x != 0:
        modulo = x % 2
        binario.append(modulo)
        x //= 2
    return binario[::-1]

def obtener_caracter_hexadecimal(valor):
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def decimal_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal



"""
Desarrollar un programa que dada una literal, forme un menú,
tal y como lo hemos visto en clase el menú que utilizamos.
"""

#Funciones ejercicio 7

def lineaSup(largo):
   linea = "   ╔"
   for i in range(1,largo-1):
      linea += "═"
   linea += "╗"
   print(linea)


def lineaMed(largo):
   linea = "   ╠"
   for i in range(1,largo-1):
      linea += "═"
   linea += "╣"
   print(linea)

   
def lineaInf(largo):
   linea = "   ╚"
   for i in range(1,largo-1):
      linea += "═"
   linea += "╝" + "\n"
   print(linea)


def lineaBlanco(largo):
   linea = "   ║"
   for i in range(1,largo-1):
      linea += " "
   linea += "║"
   print(linea)

def lineaDato(d, largo):
   linea = ""
   linea += "   ║ "
   linea += d
   blancos = largo - len(d)
   for i in range(1,blancos-2):
      linea += " "
   linea += "║"
   print(linea)
   
def menuPrincipal(literal):
   lineaSup(literal)
   lineaBlanco(literal)
   lineaDato("                          Menu",literal)
   lineaBlanco(literal)
   lineaMed(literal)
   lineaBlanco(literal)
   lineaDato("01. Ejercicio...",literal)
   lineaDato("02. Ejercicio...",literal)
   lineaDato("03. Salir",literal)
   lineaBlanco(literal)
   lineaInf(literal)



while True:
    print()
    print("""Ejercicio (1)
Ejercicio (2)
Ejercicio (3)
Ejercicio (4)
Ejercicio (5)
Ejercicio (6)
Ejercicio (7)
Salir (8)
""")
    while True:
        try:
            opc = int(input("Opción: "))
            break
        except ValueError:
            print("Valor incorrecto, volver a intentar")

    if opc == 1:
        print()
        num_1 = int(input("Digitar número: "))
        num_2 = int(input("Digitar número: "))


        print(f"Suma: {suma(num_1, num_2)}")
        print(f"Resta: {resta(num_1, num_2)}")
        print(f"Multiplicación: {mult(num_1, num_2)}")
        try:
            print(f"División: {div(num_1, num_2)}")
        except ZeroDivisionError:
            print("No se puede divir por cero")

    elif opc == 2:
        print()
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        salario_bruto = float(input("Salario: "))
        print()
        print(f"""Salario Bruto: {salario_bruto}
8% CCSS: {ccss(salario_bruto)}
1% Banco Popular: {banco(salario_bruto)}
Total deducciones: {total_deducciones(salario_bruto)}
Salario Neto: {salario_neto(salario_bruto)}
""")


    elif opc == 3:
        print()
        lado_cuadrado = float(input("Lado de un cuadrado: "))
        print(f"""Área: {area(lado_cuadrado)}
Perímetro: {peri(lado_cuadrado)}
""")

    elif opc == 4:
        print()
        num_1 = float(input("Digitar número: "))
        num_2 = float(input("Digitar número: "))
        print()
        print(f"Elevación del primero con el segundo: {elevar(num_1, num_2)}")
        
    elif opc == 5:
        print()
        precio_u = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        total = precio_u * cantidad
        print()
        print(f"Precio final con descue e IVA aplicado: {total - descuento(total) + impuesto(total)}")

    elif opc == 6:
        print()
        numero_decimal = int(input("Número decimal: "))
        hexadecimal = decimal_a_hexadecimal(numero_decimal)
        print()
        print(f"""En base binario: {decimal_binario(numero_decimal)}
En base hexadecimal: {hexadecimal}
En base octal: {decimal_octal(numero_decimal)}
""")

    elif opc == 7:
        lit = int(input("Digite un literal para formar un menú: "))
        print()
        print(menuPrincipal(lit))
    elif opc == 8:
        print()
        print("See u!")
        break
    else: 
        print("Valor fuera de rango!")
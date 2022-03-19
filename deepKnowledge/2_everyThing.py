#funcion para calcular n + nn + nnn
def suma(num):
    num += (num*11)+(num*11*10+num) #calcular n
    return num

saltar = False
while not saltar:
    print("""\nDigite algún ejercicio del (1) al (5)
Exit: (6)
""")
    opc = int(input("Ejercicio: "))

    #Obtener un conjunto de números separados por coma y crear una lista
    if opc == 1:
        numeros = input("\nnúmeros: ")
        numeros = numeros.split(",")
        print(numeros) 

    #Obtener la extensión de un archivo especificado por el usuario.
    elif opc == 2:
        nombre_archivo =  input("\nIngrese el nombre de tu archivo: ")
        nombre_archivo = nombre_archivo.split(".")
        print(nombre_archivo)
        print(f"Extensión del archivo -> {nombre_archivo[-1]}")

    #Obtener el primer y último elemento de una lista
    elif opc == 3:
        print("\nIntroduce varios lenguajes de programación")
        lenguajes = []
        for i in range(5):
            lenguaje = input("> ")
            lenguajes.append(lenguaje)
        print(f"\nStart: {lenguajes[0]} and End: {lenguajes[-1]}")

    #Mostrar la fecha de un evento almacenada en una tupla
    elif opc == 4:
        print("\nIntroduce una fecha de un evento")
        año = input("año: ")
        mes = input("mes: ")
        dia = input("día: ")
        fecha = (año,mes,dia)
        print("\nFecha: %s/%s/%s"% fecha)

    #Solicitar al usuario un número n y calcular n + nn + nnn
    elif opc == 5:
        n = int(input("Digite un número: "))
        print(f"Cálculo: {suma(n)}")

    elif opc == 6:
        print("You can do it better!")
        saltar = True
numeros = [2,4,6,8,10]
for i in range(len(numeros)-1,-1,-1):
    print(f"Índice: {i} Valor: {numeros[i]}")
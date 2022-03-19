import random

print()
print("\t\t=====================")
print("\t\t.:El Ahorcado:.")
print("\t\t=====================")
print()
print()

intentos = 7
lista_palabras = ["python", "java", "chocholate", "aprender", "estudiar", "agua", "ejercicio", "musica", "caminar",
                  "intentar", "libro", "internet", "software", "hardware", "red", "computadora", "procesador", "leer", "motherboard", "teclado","mora","fresa","love","chill","easy","learning","reading","singing","studying","monitor","dormir","comer","eat","asleep","intentar","justdoit","nice"]

palabra_aleatoria = random.choice(lista_palabras)
palabra_usuario = palabra_aleatoria

for i in palabra_usuario:
    palabra_usuario = palabra_usuario.replace(i, "_")

print(palabra_aleatoria)
print(palabra_usuario)

while True:
    print("""\t.:Opciones:.

1. Empezar el juego
2. Salir
    """)
    intentos = 5
    indice = 0
    palabra = palabra_usuario
    while True:
        try:
            opc = int(input("Opción: "))
            break
        except ValueError:
            print("Valor incorrecto. Inténtalo de nuevo")
        except NameError:
            print("Valor incorrecto. Inténtalo de nuevo")

    print()

    if opc == 1:

        while intentos != 0:

            palabra_usuario = list(palabra_usuario)

            letra = str(input("Letra -> ").lower())

            if letra.isalpha():

                if letra in palabra_aleatoria:
                    for i, l in enumerate(palabra_aleatoria):
                        if l == letra:
                            palabra_usuario[i] = letra
                    print(f"Progreso: {palabra_usuario}")

                    if palabra_usuario == list(palabra_aleatoria):
                        print()
                        print("¡Te salvaste!")
                        print("GG")
                        break

                else:
                    print()
                    print("¡Fallaste!")
                    intentos -= 1
                    print(f"Intentos restantes -> {intentos}")
                    print()
                    if intentos == 0:
                        print("¡No sobreviviste!")
            else:
                print("!Solo se permiten letras¡")

        print()

    elif opc == 2:
        print()
        print("¡You get it!")
        break

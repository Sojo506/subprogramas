import random


print()
print("\t===========================")
print("\t.:Piedra, Papel o Tijera:.")
print("\t===========================")
print()
while True:
    print("""
1. Empezar el juego
2. Salir
""")
    while True:
        try:
            opc = int(input("Escoge una opción: "))
            break
        except ValueError:
            print("¡Valor incorrecto!")
    print()
    if opc == 1:
        while True:
            try:
                escoge_usuario = input("Escoge piedra, papel o tijera: ").lower()
                break
            except ValueError:
                print("Valor incorrecto!")

        escoge_pc = random.choice(["piedra", "papel", "tijera"])

        print(f"La computadora escoge: {escoge_pc}")

        print()

        if escoge_usuario == "piedra":
            if escoge_pc == "piedra":
                print("¡Empate!")
            elif escoge_pc == "papel":
                print("¡Gana la computadora!")
            else:
                print("¡Gana el usuario!")
        elif escoge_usuario == "papel":
            if escoge_pc == "piedra":
                print("¡Gana el usuario!")
            elif escoge_pc == "papel":
                print("¡Empate!")
            else:
                print("¡Gana la computadora!")
        elif escoge_usuario == "tijera":
            if escoge_pc == "piedra":
                print("¡Gana la computadora!")
            elif escoge_pc == "papel":
                print("¡Gana el usuario!")
            else:
                print("¡Empate!")
        else:
            print("¡Te equivocaste, intenta de nuevo!")
        
        print()
    elif opc == 2:
        print("¡See u!")
        break
    else:
        print("¡Te equivocaste!")

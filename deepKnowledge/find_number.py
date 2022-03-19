import random

print("     =======================")
print("      .:Adivina el número:. ")
print("     =======================")
print()

num_azar = random.randint(0, 100)

print("\tAdina un número entre 0 y 100")

while True:

    while True:

        try:
            num_usuario = int(input("Número -> "))
            break
        except ValueError:
            print("Valor incorrecto!")

    if num_usuario == num_azar:
        print("Acertaste!")
        break
    elif num_usuario > num_azar:
        print("Disminuye!")
    elif num_usuario < num_azar:
        print("Aumenta!")

def adivina_numero_pc(x):
    from random import randint

    intentos = 0

    print("     ============================")
    print("      .:Adivina el número (PC):. ")
    print("     ============================")
    print()
    num_usuario = int(input(f"Ingresa un número entre 1 y {x}: "))
    while True:
        num_pc = randint(1, x)
        if num_pc == num_usuario:
            print(f"\nAcertaste! ({num_pc})")
            break
        elif num_pc > num_usuario:
            print(f"\nDisminuye! {num_pc}")
            intentos += 1
        elif num_pc < num_usuario:
            print(f"\nAumenta! {num_pc}")
            intentos += 1

    print(f"Intentos: {intentos}")


adivina_numero_pc(10)
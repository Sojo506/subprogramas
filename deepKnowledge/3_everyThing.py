
while True:
    print("\nEjercicios del (1) al (5)\nExit (6)")
    opc = int(input("Ejercicio -> "))
    print()
    #Obtener la documentación de funciones incorporadas
    if opc == 1:
        from math import sin
        from datetime import datetime
        print(abs.__doc__)
        print("-"*50)
        print(int.__doc__)
        print("-"*50)
        print(sin.__doc__)
        print("-"*50)
        print(datetime.now.__doc__)

    #Imprimir el calendario para un año y mes específico
    elif opc == 2:
        import calendar
        agnio = int(input("Escriba el año: "))
        mes = int(input("Escriba el mes: "))
        print(calendar.month(agnio, mes))
        print()

    #Crear una cadena de caracteres multilínea
    elif opc == 3:
        cadena = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.        
Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y,
en menor medida, programación funcional.
"""
        print(cadena)
        print()

    #Calcular la diferencia en días de dos fechas dadas
    elif opc == 4:
        from datetime import date
        hoy = date(2022,3,6)
        cumpleaños = date(2022,5,9)
        diferencia = cumpleaños - hoy
        print(diferencia.days)
    
    #Calcular el volumen de una esfera a partir del radio dado
    elif opc == 5:
        from math import pi
        r = float(input("Radio de una esfera = "))
        v = 4/3*math.pi*r**3
        print(f"Volumen = {v:.2f}")
    elif opc == 6:
        break
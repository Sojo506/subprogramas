"""
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""


notas = [70,74,80,84,60,63,50,53,40,48]
calificaciones = {}

def asignar_calificaciones(notas):
    
    for c in notas:
        if c < 60:
            calificaciones[c] = "Reprobado"
        elif c < 70:
            calificaciones[c] = "Aplazado"
        elif c >= 70:
            calificaciones[c] = "Aprobado"

    return calificaciones


print()
print(asignar_calificaciones(notas))


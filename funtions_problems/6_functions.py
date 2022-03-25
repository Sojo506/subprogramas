"""
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
"""

asig_notas = {"Cálculo": 85, "Programación": 95, "Informática": 78, "Inglés": 87, "Discretas": 70}
asig_calificadas = {}


def asignaciones(asig_datos):

    for k, v in asig_datos.items():
        if v < 60:
             asig_calificadas[k.upper()] =  "Reprobado"
        elif v < 70:
             asig_calificadas[k.upper()] =  "Aplazado"
        elif v >= 70:
             asig_calificadas[k.upper()] =  "Aprobado"
    
    return asig_calificadas


print()
print("  ========================================================================================================================")
print(asignaciones(asig_notas))
print("  ========================================================================================================================")
       
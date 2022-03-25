"""
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
"""

frase = "La magia, florece, solo en almas únicas, se le otorga, a quienes tienen destinos importantes"



def get_frase(frase):

    palabras = frase.split()
    longitud = map(len, palabras)

    
    return dict(zip(palabras,longitud))

        

print(get_frase(frase))
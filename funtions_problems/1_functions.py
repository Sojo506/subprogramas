def descuento(precio,desc): 
    return precio - precio * desc // 100



def impuesto(precio,iva):
    return precio + precio * iva // 100



def productos(compra):
    total_antes = 0
    total_despues = 0

    for p,d,i in compra.values():
        total_antes += p
    

    for p,d,i in compra.values():
        opc_1 = descuento(p, d)
        opc_2 = impuesto(opc_1, i)
        total_despues += opc_2

    return f'''Sin aplicar el descuento y el IVA: ¢{total_antes}
Con el descuento y el iva aplicado: ¢{total_despues}    
'''



cesta = {"Yogurt":[2600, 20, 13],"Cereal":[4650, 15, 13], "Pan integral": [4950, 16, 13], "Galletas": [7600, 14, 13],"Avena": [3600, 18, 13]}

print()
print(f'''\t\t:Resultado:. 
{productos(cesta)}''')
# Un negocio comercializa un articulo cuyo precio es 3.000
# y de acuerdo a la cantidad vendida efectua diferentes descuentos:
# 1. si 0 < cantidad_vendida <= 10 no se hace descuento
# 2. si 11 <= cantidad_vendida < 20 se hace un 2% de descuento
# 3. si cantidad vendida > 19 se hace un 4% de descuento
# informar cuanto percibio por la venta efectuada

import math
precio_unitario = 3000
cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

if cantidad_vendida > 0 and cantidad_vendida <= 10:
    print(f'El precio total es de {precio_unitario} pesos.')
if cantidad_vendida > 10 and cantidad_vendida <= 19:
    descuento = math.floor(precio_unitario - ((precio_unitario * 2)/ 100))
    precio_final = cantidad_vendida * descuento
    print(f'El precio total es de {precio_final} pesos.')
if cantidad_vendida > 19:
    descuento = math.floor(precio_unitario - ((precio_unitario * 4)/ 100))
    precio_final = cantidad_vendida * descuento
    print(f'El precio total es de {precio_final} pesos.')
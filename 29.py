"""Una organizacion comercial compra directamente de fabrica,
 y de acuerdo a la cantidad comprada recibe diferentes bonificaciones
 
 si cant_comprada <= 1000 unidades = Bonificacion: 5 unidades
 si 1000 < cant_comprada < 1501 unidades = Bonificacion: 2% de unidades
 si 1500 < cant_comprada <= 2000 unidades = Bonificacion: 3% de unidades
 si cant_comprada > 2000 unidades = Bonificacion: 100 unidades
 
 Informar: La cantidad de unidades que recibe en total"""
import math

cant_comprada = int(input("Ingrese la cantidad de unidades compradas: "))

if cant_comprada <= 1000:
    bonificacion = 5
    total = cant_comprada + bonificacion
elif cant_comprada > 1000 and cant_comprada > 1501:
    bonificacion = math.floor((cant_comprada * 2) / 100)
    total = cant_comprada + bonificacion
elif cant_comprada > 1500 and cant_comprada <= 2000:
    bonificacion = math.floor((cant_comprada * 3) / 100)
    total = cant_comprada + bonificacion
else:
    bonificacion = 100
    total = cant_comprada + bonificacion
print(total)
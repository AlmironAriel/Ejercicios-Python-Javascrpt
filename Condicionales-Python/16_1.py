"""Construir un algoritmo que permita leer un numero entero de tres digitos
y determinar si el primer digito es multiplo de los otros dos"""

import math

num = int(input('Ingrese un numero de tres digitos: '))

if num>99 and num<1000:
    centena = math.floor(num/100)
    decena = math.floor((num - (centena * 100)) / 10)
    unidad = math.floor((num - (centena * 100)) - (decena * 10))
    if centena % decena == 0 and centena % unidad == 0:
        print('El primer digito es multiplo de los otros dos digitos')
    else:
        print('El primer digito no es multiplo de los otros dos digitos.')
else:
    print('por favor ingrese un numero de tres cifras.')
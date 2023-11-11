"""Construir un algoritmo que permita leer un numero enteo de dos digitos
determinar a cuanto es igual la suma de sus dos digitos"""

import math

num = int(input('Ingrese un numero entero de dos digitos: '))
if num>9:
    digito_1 = num // 10 #// funciona como math.floor 
    digito_2 = num % 10 #modulo, residuo de un numero / 10
    suma = digito_1 + digito_2
    print(f'La suma de ambos digitos es {suma}')
else:
    print('Por favor ingrese un numero de dos cifras.')


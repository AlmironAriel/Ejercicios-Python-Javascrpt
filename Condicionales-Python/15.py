"""Construir un algoritmo que permita leer un numero entero de dos digitos
y determinar si sus dos digitos son iguales"""

import math

num = int(input('Ingrese un numero entero de dos digitos: '))
if num>9:
    digito_1 = num // 10 #// funciona como math.floor 
    digito_2 = num % 10 #modulo, residuo de un numero / 10
    if digito_1 == digito_2:
        print(f'Los dos digitos de {num} son iguales.')
else:
    print('Por favor ingrese un numero de dos cifras.')
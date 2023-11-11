"""Construir un algoritmo que permita leer un numero
entero positivo de un digito y determinar si ese numero es un numero primo"""

num = int(input('Ingrese un numero entero positivo: '))

if num >= 0 and num < 10:
    if num==2 or num==3 or num==5 or num==7:
        print('Es un numero primo')
    else:
        print('No es un numero primo')
else:
    print('por favor ingrese un numero entero positivo de 1 digito.')


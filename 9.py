# Construir un algoritmo que permita leer un numero entero y determinar si es de dos digitos

num = int(input('Ingrese un numero entero: '))

if num>-10 and num<10:
    print('El numero ingresado tiene 1 digito.')
else:
    print('El numero ingresado tiene 2 digitos.')


"""Ingresar tres numeros mayores a cero. validar los datos. multiplicarlos entre si, informar:
1. ¿El resultado es multiplo de 3?
2. ¿Cuantos numeros pares s ingresaron?"""

pares = 0
multiplo = False
num_1 = int(input('Ingrese el primer número positivo: '))
num_2 = int(input('Ingrese el segundo número positivo: '))
num_3 = int(input('Ingrese el último número positivo: '))

if num_1 > 0 and num_2 > 0 and num_3 > 0:
    multiplicacion = num_1 * num_2 * num_3
    if multiplicacion % 3 == 0:
        multiplo = True
    if num_1 % 2 == 0:
        pares += 1
    if  num_2 % 2 == 0:
        pares += 1
    if num_3 % 2 == 0:
        pares += 1

    if multiplo == True:
        print('El resultado de la multiplicacion de los numeros es multiplo de 3.')
    else:
        print('El resultado de la multiplicacion de los numeros no es multiplo de 3.')

    print('Se ingresaron ' + str(pares) + ' numeros pares.')

else:
    print('Por favor ingrese un numero mayor a cero.')

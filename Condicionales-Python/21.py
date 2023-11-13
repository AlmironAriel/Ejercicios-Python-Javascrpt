# se ingresan dos numeros, se informa el menor

num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num_1 < num_2:
    print('El numero', num_1, 'es menor que el numero', num_2)
else:
    print('El numero', num_2, 'es menor que el numero', num_1)
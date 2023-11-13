#  Construir un algoritmo que permita leer dos numeros enteros y determinar si uno es multiplo del otro

num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num_1 % num_2 == 0:
    print(f'{num_1} es multiplo de {num_2}')
elif num_2 % num_1 == 0:
    print(f'{num_2} es multiplo de {num_1}')
else:
    print('Ningun numero es multiplo del otro.')
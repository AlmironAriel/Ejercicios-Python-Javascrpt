 # Ingresar dos numeros positivos y sumarlos. Validar os datos. Informar:
# ¿Cuantos numeros impares se ingresaron?
# ¿La suma es multiplo de dos?

impar = 0
suma = 0
multiplo = False
num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num_1 > 0 and num_2 > 0:
    suma = num_1 + num_2
    if num_1 % 2 == 1 or num_2 % 2 == 1:
        impar += 1
    elif suma % 2 == 0:
        multiplo = True

    print('Se ingresaron ' + str(impar) + ' numeros impares.')

    if multiplo == True:
        print('La suma de ambos numeros es multiplo de 2.')
    else:
        print('La suma de ambos numeros no es multiplo de 2.')
else:
    print('Por favor ingrese numeros positivos.')



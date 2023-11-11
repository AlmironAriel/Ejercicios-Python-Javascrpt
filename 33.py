 # Ingresar tres numeros, informar
 # En los numeros ingresados hay algn negativo?
 # En los numero ingresados hay algun numero que pertenezca a los intervalos
 # ...de valores desde el 23 al 37?

negativo = False
num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))
num_3 = int(input('Ingrese el tercer numero: '))


if num_1 < 0 or num_2 < 0 or num_3 < 0:
    print('Se ingresaron numeros negativos.')
if num_1 > 22 and num_1 < 38:
    print('El numero ' + str(num_1) + ' pertenece al intervalo desde 23 al 37.')
if num_2 > 22 and num_2 < 38:
    print('El numero ' + str(num_2) + ' pertenece al intervalo desde 23 al 37.')
if num_3 > 22 and num_3 < 38:
    print('El numero ' + str(num_3) + ' pertenece al intervalo desde 23 al 37.')

if negativo == True:
    print('Entre los numeros ingreados hay umeros negativos.')



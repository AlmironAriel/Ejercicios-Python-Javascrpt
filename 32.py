 # Ingresar dos numeros y multiplicarlos entre si. Informar:
 # ¿El resultado es positivo?
 # ¿Alguno de los numeros ingresados es cero?

num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

multiplicacion = num_1 * num_2

if multiplicacion > 0:
    print('La multiplicacion de ambos numeros es positiva')

if num_1 == 0 and num_2 == 0:
    print('Ambos numeros son 0')
elif num_1 == 0:
    print('El primer numero ingresado es un 0.')
elif num_2== 0:
    print('El segundo numero ingresado es un 0.')
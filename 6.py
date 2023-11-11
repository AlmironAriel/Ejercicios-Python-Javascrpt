"""Se ingresa al proceso dos numeros enteros y un codigo de operacion, 
(1=suma, 2=multipliacion, 3=diferencia). 
Se desea obtener el resultado de la operacion realizada y un texto el cual declaro cual fue esa operacion."""

num_1 = int(input('Ingrese el primer nùmero: '))
num_2 = int(input('Ingrese el segundo nùmero: '))
opcion = int(input('Eliga la operacion a realizar: 1=SUMA, 2=MULTIPLICACION, 3=DIFERENCIA: '))

if opcion == 1:
    operacion = num_1 + num_2
    print('La suma de ambos nùmeros es: ' + str(operacion))
elif opcion == 2:
    operacion = num_1 * num_2
    print('La multiplicacion de ambos nùmeros es: ' + str(operacion))
elif opcion == 3:
    operacion = num_1 - num_2
    print('La diferencia entre ambos nùmeros es : ' + str(operacion))

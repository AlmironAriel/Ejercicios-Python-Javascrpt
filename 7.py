"""Se ha determinado que despues del uso del programa el operador es falible.
mantener el programa del ejercicio enterior, tal que muestre un mensaje de error
en el caso de que el còdigo de operaciòn sea fuera de rango"""

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
else:
    print('La opcion ingresada esta fuera de rango.')
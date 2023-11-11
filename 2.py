"""Mantener el programa anterior
 de tal manera que se pueda saber si todos los niños recibieron la misma cantidad de caramelos.
   siendo los niños y los caramelos valores no constantes en cada ingreso"""

import math

caramelos = int(input('Ingrese la cantidad de caramelos a repartir: '))
ninios = int(input('Ingrese el numero de niños: '))

if caramelos % ninios == 0:
    print('Todos los niños recibieron la misma cantidad de caramelos.')
else:
    print('Los niños no recibieron cantidades iguales de caramelos.')
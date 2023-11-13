# Mantener el programa anterior el cual detecta la no existencia de caramelos y genere una salida acorde a esa sircunstancia

caramelos = int(input('Ingrese la cantidad de caramelos a repartir: '))

if caramelos > 0:
    ninios = int(input('Ingrese la cantidad de niños: '))
    if caramelos % ninios == 0:
        print('Los niños recibieron la misma cantidad de caramelos.')
    else:
        print('Los niños no recibieron la misma cantidad de caramelos.')
else: 
    print('Por favor ingrese un numero mayor a cero.')

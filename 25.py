"""Ingresar dos valores numericos que representan las coordenadas cartesianas
de un punto en el plano x, y. Se desea determinar en que cuadrante se encuentra"""

eje_x = int(input('Ingresa un valor para el eje X: '))
eje_y = int(input('Ingresa un valor para el eje Y: '))

if eje_x > 0 and eje_y > 0:
    print(f'El punto ({eje_x}:{eje_y}) pertenece al Primer Cuadrante')
elif eje_x < 0 and eje_y > 0:
    print(f'El punto ({eje_x}:{eje_y}) pertenece al Segundo Cuadrante')
elif eje_x < 0 and eje_y < 0:
    print(f'El punto ({eje_x}:{eje_y}) pertenece al Tercer Cuadrante')
else:
    print(f'El punto ({eje_x}:{eje_y}) pertenece al Cuarto Cuadrante')


 #  Eje X positivo, eje Y positivo = 1er cuadrante
 #  Eje X negativo, eje Y positivo = 2do cuadrante
 #  Eje X negativo, eje Y negativo = 3er cuadrante
 #  Eje X positivo, eje Y negativo = 4to cuadrante
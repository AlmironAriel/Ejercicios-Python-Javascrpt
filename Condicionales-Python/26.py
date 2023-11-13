 #  Se ingresan 4 calificaciones de un alumno, informar el promedio de las 3 mejores

import math
suma = 0

a = int(input('Ingrese primera la nota: '))
b = int(input('Ingrese la segunda nota: '))
c = int(input('Ingrese la tercera nota: '))
d = int(input('Ingrese la ultima nota: '))

if a < b and a < c and a < d:
    menor = a
elif b < a and b < c and b < d:
    menor = b
elif c < a and c < b and c < d:
    menor = c
elif d < a and d < b and d < c:
    menor = d

suma = ((a + b + c + d) - menor)
promedio = math.floor(suma / 3)

print("El promedio de las tres mejores notas es " + str(promedio))
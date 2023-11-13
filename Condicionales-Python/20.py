"""Escribir un prorama que dado los cuatro lados de un triangulo: A, B, y C determine que tipo es.
Suponiendo que A sea el mayor de sus lados, usar la siguiente tabla para la resolucion del problema:
- si A >= B + C entonces no forma un triangulo
- si A^2 = B^2 + C^2 entonces forma un triangulo rectangulo 
- si A^2 > B^2 + C^2 entonces forma un triangulo obtuso
- si A^2 < B^2 + C^2 entonces forma un triangulo agudo
- si A^2 = B^2 = C^2 entonces forma un triangulo equilatero"""

a = int(input('Ingrese la medida del primer lado del angulo: '))
b = int(input('Ingrese la medida del segundo lado del angulo: '))
c = int(input('Ingrese la medida del tercer lado del angulo: '))

if a >= (b + c):
    print('Las medidas de los lados no forman un triangulo')
elif a**2 == (b**2 + c**2):
    print('Los lados forman un triangulo rectangulo')
elif a**2 > (b**2 + c**2):
    print('Los lados forman un triangulo obtuso')
elif a**2 < b**2 + c**2:
    print('Los lados forman un rectangulo agudo')
elif a**2 == b**2 and a**2 == c**2:
    print('Los lados forman un rectangulo equilatero')

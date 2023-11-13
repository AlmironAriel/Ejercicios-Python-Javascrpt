# Ingresar las medidas de los lados de un triangulo
# Informar si es escaleno, isosceles  o equilatero

a = float(input('Ingresa la medida del lado  A del triangulo: '))
b = float(input('Ingresa la medida del lado B del triangulo: '))
c = float(input('Ingresa la medida del lado C del triangulo: '))

if (a == b and b == c):
    print('El triangulo es equilatero')
if (a == b or b == c or c == a):
    print('El triangulo es isosceles')
else:
    print('El triangulo es escaleno')
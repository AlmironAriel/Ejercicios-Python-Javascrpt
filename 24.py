"""Se ingresan 5 valores a,b,c,d,e y un codigo.
informar segun sea el codigo:
codigo = 1  informar = a + b + c + d + e
codigo = 2  informar = a + b + c + d - e
codigo = 3  informar = a + b

no habra otros codigos
"""

a = int(input('Ingrese el primer valor: '))
b = int(input('Ingrese el segundo valor: '))
c = int(input('Ingrese el tercer valor: '))
d = int(input('Ingrese el cuarto valor: '))
e = int(input('Ingrese el ultimo valor: '))

codigo = int(input('Ingrese codigo 1 / 2 / 3: '))

if codigo == 1:
    resultado = ((((a + b) + c) + d) + e)
    print(resultado)
elif codigo == 2:
    resultado = ((((a + b) + c) + d) - e)
    print(resultado)
elif codigo == 3:
    resultado = a + b
    print(resultado)
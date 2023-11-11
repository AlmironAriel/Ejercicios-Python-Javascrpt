"""Construir un programa que lea un numero de cuatro o mas cifras
 y los separe en digitos"""

num = input('Ingrese un numero de varios digitos: ') # Ejemplo 1234
list = []

for digito in num:
    list.append(int(digito))
print(list) # Imprimiria [1, 2, 3, 4]

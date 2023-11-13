"""De una exposicion de libros se conocen las cantidades de libros de autores argentinos,
latinoamericanos, europeos y asiaticos que hay. se decide hacer un programa que informe:
1. La cantidad de libros que hay en la exposicion
2. Que porcentaje del total le correspondia a cada una de las cantidades ingresadas
3. Cual es el nvel de la exposicion, considerando que puede ser:
MALO, BUENO, MUY BUENO, EXELENTE o SOBRESALIENTE. si las cantidades de obras expuestas es menor que:
5.000, 10.000, 20.000, 30.000 o 40.000 respectivamente."""

import math

lbrs_argen = int(input('Ingrese el numero de libros argentinos: '))
lbrs_lat_amer = int(input('Ingrese el numero de libros latinoamericanos: '))
lbrs_euro = int(input('Ingrese el numero de libros europeos: '))
lbrs_asia = int(input('Ingrese el numero de libros asiaticos: '))

total_lbrs = ((((lbrs_argen + lbrs_lat_amer) + lbrs_euro) + lbrs_asia))

porc_lbrs_arg = math.floor((lbrs_argen*100)/ total_lbrs)
porc_lbrs_lat_amer = math.floor((lbrs_lat_amer*100)/ total_lbrs)
porc_lbrs_euro = math.floor((lbrs_euro*100)/ total_lbrs)
porc_lbrs_asia = math.floor((lbrs_asia*100)/ total_lbrs)

if total_lbrs < 5000:
    nivel_expo = 'MALO'
elif total_lbrs < 10000:
    nivel_expo = 'BUENO'
elif total_lbrs < 20000:
    nivel_expo = 'MUY BUENO'
elif total_lbrs < 30000:
    nivel_expo = 'EXELENTE'
else:
    nivel_expo = 'SOBRESALIENTE'

 #  Resultados

print('')
print(f'La cantidad total en la exposicion es de {total_lbrs} libros.')
print('')
print(f'El porcentaje de libros argentinos en la exposicion es de {porc_lbrs_arg}%;\nLos libros latinoamericanos represnetan el {porc_lbrs_lat_amer}%;\nLos libros europeos, el {porc_lbrs_euro}%\ny los libros de autores asiaticos el {porc_lbrs_asia}% del total de libros de la exposicion.')
print(f'Por o tanto, el nivel de la exposicion fue {nivel_expo}.')

#  \n es un enter o salto de linea

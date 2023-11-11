"""Ingresar las ventas totales que efectuo un empleado durante una quincena.
informar la comision que le corresponde en pesos segun sea el caso:
si 0 < ventas <= $5.000 no tiene comision
si $ 5.000 < ventas <= $10.000 comision del 8% sobre las ventas
si ventas > $10.000 comision de 5% sobre la diferencia entre la venta total y $10.000, mas $800 fijos."""

import math

ventas = int(input('Ingrese el monto de ventas realizadas en una quincena: '))

if ventas > 0 and ventas <= 5000:
    print('Al vendedor no le toca comision')
elif ventas > 5000 and ventas <= 10000:
    comision = math.floor((ventas * 8)/ 100)
    print('Al vendedor le toca una comision de',comision,'pesos.')
elif ventas > 10000:
    comision = math.floor((((ventas - 10000)* 5) / 100) + 800)
    print('Al vendedor le toca una comision de',comision,'pesos.')

 #  Math.floor redondea la cifra hacia abajo y elimina los decimales para entregar un numero mas limpio
 #  Se importa la funcion Math.floor de la libreria math.

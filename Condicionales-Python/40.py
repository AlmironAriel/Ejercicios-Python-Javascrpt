# ingresar la cantidad de horas trabajadas por un empleado,
# la categoria en la que se desempeña, y un numero de empleado, se debe calcular y luego informar: 
# 1. sueldo del empleado
# 2. el numero del empleado y su sueldo si este supera a los $1500
# valor por hora es de: categorias 1, 2 y 3, pesos 20, 25 y 33 respectivamente

horas_trabajadas = int(input('Ingrese las horas trabajadas por el empleado: '))
categoria_empleado = int(input('Ingrese la categoria del empledo: '))
numero_empleado = int(input('Ingrese el numero del empleado: '))

sueldo_hora_categoria1 = 20
sueldo_hora_categoria2 = 25
sueldo_hora_categoria3 = 33

if categoria_empleado == 1:
    sueldo = sueldo_hora_categoria1 * horas_trabajadas
    print(f'El sueldo del empleado es de {sueldo} pesos.')
    if sueldo > 1500:
        print(f'El sueldo del empleado numero {numero_empleado} es de {sueldo} pesos.')
elif categoria_empleado == 2:
    sueldo = sueldo_hora_categoria2 * horas_trabajadas
    print(f'El sueldo del empleado es de {sueldo} pesos')
    if sueldo > 1500:
        print(f'El sueldo del empleado numero {numero_empleado} es de {sueldo} pesos.')
else:
    sueldo = sueldo_hora_categoria3 * horas_trabajadas
    print(f'El sueldo del empleado es de {sueldo} pesos')
    if sueldo > 1500:
        print(f'El sueldo del empleado numero {numero_empleado} es de {sueldo} pesos.')


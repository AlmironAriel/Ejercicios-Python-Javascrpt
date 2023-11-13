# se ingresa la primera letra de los apellidos de 3 alumnos.
# informarlas en forma ordenada ascendente sin hacer intercambio de valores 

letra1 = input('Ingrese la primera inicial: ')
letra2 = input('Ingrese la segunda inicial: ')
letra3 = input('Ingrese la tercera inicial: ')

if letra1 > letra2:
    if letra2 > letra3:
        print(f'{letra3} {letra2} {letra1}')
    elif letra1 > letra3:
        print(letra1, letra2, letra3)
    else:
        print(letra2, letra1, letra3)
else:
    if letra1 > letra3:
        print(letra3, letra1, letra2)
    elif letra2 > letra3:
        print(letra1, letra3, letra2)
    else:
        print(letra1, letra2, letra3)
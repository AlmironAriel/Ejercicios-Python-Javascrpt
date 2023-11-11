"""simular una tirada de dados y ver si se produce generala. Realizarlo de dos formas:

- Comparando los dados de a dos
- Comparando los cinco dados simultaneamente"""

dado_1  = int(input('Del 1 al 6 ingresar un valor para el dado 1: ')) 
dado_2  = int(input('Del 1 al 6 ingresar un valor para el dado 2: '))
dado_3  = int(input('Del 1 al 6 ingresar un valor para el dado 3: '))
dado_4  = int(input('Del 1 al 6 ingresar un valor para el dado 4: '))
dado_5  = int(input('Del 1 al 6 ingresar un valor para el dado 5: '))

if dado_1 == dado_2 and dado_3 == dado_4 and dado_1 == dado_5:
    print('¡Felicidades! ¡ganaste 60 puntos! ¡Haz sacado GENERALA!')
else:
    print('Sigue tirando dados!')

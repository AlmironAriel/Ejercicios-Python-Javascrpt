 # se ingresan 4 calificaciones de un alumno, informar el promedio de las tres peores

import math
nota1 = int(input("Ingrese la nota del alumno: "))
nota2 = int(input("Ingrese la nota del alumno: "))
nota3 = int(input("Ingrese la nota del alumno: "))
nota4 = int(input("Ingrese la nota del alumno: "))

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    mayor = nota1
    suma = nota2 + nota3 + nota4
elif nota2 > nota1 and nota2 > nota3 and nota1 > nota4:
    mayor = nota2
    suma = nota1 + nota3 + nota4
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    mayor = nota3
    suma = nota1 + nota2 + nota4
else:
    mayor = nota4
    suma = nota1 + nota2 + nota3

promedio = math.floor(suma / 3)
print(f"El promedio de las tres peores notas es {promedio}")
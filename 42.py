"""Ingresar las edades y la estatura de tres alumnos de un curso de primer año de la 
tecnicatura superior en istalación y mantenimiento de sistemas de computo. se pide: 
1. informar la edad promedio
2. informar la estatura promedio
3. informar las edades de los alumnos mayores de 20 años que miden menos de 1.60 mts."""

import math

edad1 = int(input("Ingrese la edad del primer alumno: "))
estatura1 = float(input("Ingresar la estatura del primer alumno: "))
edad2 = int(input("Ingrese la edad del segundo alumno: "))
estatura2 = float(input("Ingresar la estatura del segundo alumno: "))
edad3 = int(input("Ingrese la edad del tercer alumno: "))
estatura3 = float(input("Ingresar la estatura del tercer alumno: "))
 # Edad promedio
edad_suma = edad1 + edad2 + edad3
promedio_edad = math.floor(edad_suma / 3)

 # Estatura promedio
estatura_suma = estatura1 + estatura2 + estatura3
promedio_estatura = math.floor(estatura_suma / 3)

print("")
print(f"La edad promedio de los alumnos es de {promedio_edad} años.")
print(f"La estatura promedio de los alumnos es de {promedio_estatura} metros.")
print("Las edades de los alumnos mayores a 20 años y menores de 1.60 mts:")

 # Edades de los alumnos mayores a 20 años que miden menos de 1.60mts
if edad1 > 20 and estatura1 < 1.60:
    print(edad1)
elif edad2 > 20 and estatura2 < 1.60:
    print(edad2)
elif edad3 > 20 and estatura3 < 1.60:
    print(edad3)
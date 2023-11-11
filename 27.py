"""Ingresar una calificación numérica e informar el concepto según la siguiente tabla
Nota = 0.00 a 3.99      Informar INSUFICIENTE
Nota = 4.00 a 6.99      Informar REGULAR
Nota = 7.00 a 8.99      Informar BUENO
Nota = 9.00 a 10.00     Informar MUY BUENO"""

nota = float(input('Ingrese la nota del alumno con sus decimales: '))

if nota >= 0.00 and nota <= 3.99:
    print("INSUFICIENTE")
elif nota >= 4.00 and nota <= 6.99:
    print("REGULAR")
elif nota >= 7.00 and nota < 8.99:
    print("BUENO")
else:
    print("MUY BUENO")
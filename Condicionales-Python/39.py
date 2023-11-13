# se tiene un numero N, informar si es par y multiplo de 7.

num = int(input("Ingrese un número: "))

if  num % 2 == 0 and num % 7 == 0:
    print(f"El numero {num} es par y es multiplo de 7")
else:
    print(f"El numero {num} puede que no sea par o que no sea multiplo de 7")
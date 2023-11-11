# realizar un programa que permita ingresar 3 datos, (que son valores de distancias entre localidades). 
# informar la mayor distancia ingresada 

distancia_1 = int(input("Ingrese el primer valor de distancia: "))
distancia_2 =int(input("Ingrese el segundo valor de distancia: "))
distancia_3 = int(input("Ingrese el tercer valor de distancia: "))

if distancia_1 > distancia_2 and distancia_1 > distancia_3:
    mayor = distancia_1
elif distancia_2 > distancia_1 and distancia_2 > distancia_3:
    mayor = distancia_2
else:
    mayor = distancia_3

print(f"La mayor disttaancia entre localidades es de {mayor}")
"""Se leen dos nùmeros A y B, y se pide imprimir:
-1 si A<0 y B<0
1 si A>0 y B>0
0 si A*B<=0"""

A = int(input('Ingrese el primer numero: '))
B = int(input('Ingrese el segundo numero: '))

if A<0 and B<0:
    print('-1')
elif A>0 and B>0:
    print('1')
elif (A*B)<=0:
    print('0')


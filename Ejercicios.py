######Estructuras Iterativas:
'''
Problema 1
'''
inicio = 1500
fin = 2700
for i in range(inicio,fin,1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
'''
Problema 2
'''
fila = 5
for i in range(fila * 2 - 1):
    if i < fila:
        print('* '* (i + 1))
    else: 
        print('* '* (2 * fila - i - 1))
'''
Problema 3
'''
p = input('¿Desea ingresar un número?:  ').lower()
lista = []

while p == 'si':
    n1 = int(input('Ingrese el número: '))
    lista.append(n1)
    p = input('¿Desea ingresar un número?:  ').lower()
print('Números ingresados: ',lista)

pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    elif i % 2 != 0:
        impares.append(i)

print('Cantidad de números pares: ',len(pares))
print('Cantidad de números impares: ',len(impares))
'''
Problema 4
'''







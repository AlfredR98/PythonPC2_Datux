###### Estructuras Iterativas:
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
alum_notas = {}
lnotas = []
z = 1

registros = int(input('Ingrese la cantidad de alumnos que va a registrar: '))

while z <= registros:
    nombre = input(f'Ingrese el nombre del alumno {z}: ')
    alum_notas[f'Alumno{z}'] = nombre

    for i in range(3):
      notas = int(input(f'Ingrese la nota {i+1}: '))
      lnotas.append(notas)

    alum_notas[f'Notas{z}'] = lnotas
    z+=1

print(alum_notas)
###### Funciones:
'''
Problema 5
'''
def contar_digito(numero,digito):
    dig = numero.count(digito)
    return dig

numero = input('Ingrese número: ')

while True:
  digito = input('Ingrese el dígito para saber cuantas veces se repite: ')
  if len(digito) == 1:
     contar = contar_digito(numero,digito)
     print('El número ingresado es:\t ',numero)
     print(f'El dígito {digito} se repite en el número: {contar} veces')
     break
  else:
     print('!! Debe ingresar solo 1 dígito !!\n')
  continue
'''
Problema 6
'''






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
def fibonacci(num):
    valores = [0, 1]
    while valores[-1] + valores[-2] <= num:
        valores.append(valores[-1] + valores[-2])
    return valores

secuencia_fibonacci = fibonacci(50)

print("Serie Fibonacci :")
print(secuencia_fibonacci)
'''
Problema 7
'''
def validar_primo(num):   
    primo = True
    for i in range(2, num):
        if num % i == 0:
            # encontre un divisor
            primo = False
            break
    return primo

num_primo = int(input('Ingrese número a evaluar: '))

if validar_primo(num_primo):
    print(f'El número {num_primo} es primo' )
else:
    print(f'El número {num_primo} no es primo')

'''
Problema 8
'''
def calculo_factorial(num):
    fac = 1
    for i in range(num):
        fac *=(i+1)
    return fac

while True:
    numero = int(input('Ingrese el número a calcular: '))
    if numero <= 0:
            print('Ingrese número mayor a 0')
            continue
    else:
        factorial = calculo_factorial(numero)  
        print(f"El factorial de {numero} es:  {factorial}")
        break
'''
Problema 9
'''
def quitar_vocales(texto):
    vocales = "aeiouAEIOU"
    textoNoVocales = ''.join([char for char in texto if char not in vocales])
    return textoNoVocales

mensaje = input("Ingrese el texto:\n")

r = quitar_vocales(mensaje)
print("Resultado:", r)
'''
Problema 10
'''



alum_notas = {}
lnotas = []
z = 1
registros = int(input('Ingrese la cantidad de alumnos que va a registrar: '))


while z <= registros:
    nombre = input(f'Ingrese el nombre del alumno {z}: ')
    for i in range(3):
      notas = int(input(f'Ingrese la nota {i+1}: '))
      lnotas.append(notas)
  
    z+=1
alum_notas['Alumno'] = nombre
alum_notas['Notas'] = lnotas
print(alum_notas)




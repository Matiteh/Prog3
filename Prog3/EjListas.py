import random


#1
"""list=[]
cuadrado=0
cubo=0
for i in range(10):
    list.append(random.randint(0, 10))
    cuadrado=pow(list[i],2)
    cubo=pow(list[i],3)
    print('El numero es: ',list[i],', Su cuadrado es: ',cuadrado,', Su cubo es: ',cubo)"""
#2
"""list1=[]
list2=[]
cadena=''
for i in range(5):
    cadena=str(input('Ingrese la cadena %d\n'%(i+1)))
    list1.append(cadena)
    
    if i==4:
        list2=list1.copy()
        list2.reverse()
        print('Lista 1: ',list1,'\n Lista 2: ',list2,)"""
#3
"""list=[]
nota=0
promNota=0
maxNota=0
minNota=0
for i in range(5):
    nota=str(input('Ingrese la nota %d\n'%(i+1)))
    list.append(nota)
    promNota=promNota+int (list[i])
    if i==4:
        maxNota=max(list)
        minNota=min(list)
        promNota=promNota/len(list)
        print('Las Notas son: ',list, '\n El promedio de notas es: ',promNota, '\n La nota max es: ',maxNota, '\n La nota min es: ',minNota)"""

#4
"""list=[]
num=0
while num >=0:
    num=int(input('Ingrese un numero \n'))
    list.append(num)
list.pop(-1)
print('Los numeros ingresados son: ',list)"""
#5
"""list=[]
for i in range(10):
    list.append(random.randint(0,200))
list.sort()
print('Estos son los numeros de la lista ordenados de menor a mayor: ',list)"""

#6
"""list=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
lista=['31','28','31','30','31','30','31','31','30','31','30','31',]
mes=int (input('Ingrese numero de mes: '))
print('El mes es: ',list[mes-1],'\n y tiene ',lista[mes-1],'dias')"""

#7
"""list1=[]
list2=[]
list3=[]
num=0
for i in range(5):
    num=int(input('Ingrese el numero %d de la lista1: '%(i+1)))
    list1.append(num)
    num=int(input('Ingrese el numero %d de la lista2: '%(i+1)))
    list2.append(num)
    list3.append(list1[i]+list2[i])
print('La suma de la lista 1 y la lista 2 es: ',list3)"""


#8
"""listN=[]
listE=[]
nombre=''
edad=0
i=0
while nombre != '*':
    nombre=str(input('Ingrese nombre del estudiante %d: '%(i+1)))
    if nombre !='*':
        listN.append(nombre)
        listE.append(int(input('Ingrese edad del estudiante %d: '%(i+1))))
    else:
        i=0
        break
    i+=1
print('Los alumnos mayores de edad son: ')
for i in range(len(listN)):
    if listE[i] >=18:
        print(listN[i])
    if edad < listE[i]:
        edad = listE[i]
print('Los alumnos con la edad maxima son: ')
for i in range(len(listE)):
    if listE[i]== edad:
        print(listN[i])"""

#10
tabla=[]
sumtabla=[]
sumtablacol=[]
for i in range(5):
    fila=[]
    for j in range(5):
        fila.append(random.randint(0, 15))
    tabla.append(fila)
    sumtabla.append(sum(tabla[i]))
for col in range(5):
    suma=0
    for fila in tabla:
        suma= suma+ fila[col]
    sumtablacol.append(suma)

print('Esta es la tabla: ',tabla)
print('Esta es la suma de la tabla por fila: ',sumtabla)
print('Esta es la suma de la tabla por columna: ',sumtablacol)
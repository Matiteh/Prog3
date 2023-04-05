cantNumeros=int (input("Ingrese la cantidad de iteraciones:"))
"""F1=1
F2=1
i=0
while i < (cantNumeros):
    sumaAnteriores= 0
    if i==0: 
        print(F1)
    elif i==1:
        print(F2)
    else:
        sumaAnteriores= F1+F2
        print(sumaAnteriores)
        F1=F2
        F2=sumaAnteriores
    i+=1"""


num=1
resulSumN=0
resulSumP=0
cantP=0
promP=0
i=0

for i in range(cantNumeros):
    resulNum= 0
    numPot= num
    if num%2 ==1: 
        num = -abs(num)
    elif num%2 ==0:
        num = abs(num)
    resulNum= num**numPot
    print(num,'^',numPot, '=', resulNum)

    if num>=0:
        cantP+=1
        resulSumP= resulSumP+resulNum
    else:
        resulSumN= resulSumN+resulNum
    num=abs(num)
    num+=1
    i+=1
print("La suma de los numeros negativos es: ",resulSumN)

promP=resulSumP/cantP
print("El promedio de los numeros positivos es: ",promP)
import time
nums=int(input("Ingrese la cantidad de numeros a ser sumados: "))
i=1
suma_final=0
while i<=nums:
    num1=int(input("Ingrese el numero "+str(i)+" : "))
    suma_final=suma_final+num1
    i=i+1

else:
    print(suma_final)

import time
num1=int(input("Por favor ingrese el primer numero: "))
num2=int(input("Por favor ingrese el segundo numero: "))


while (num2<=num1):
    num2=int(input("Por favor ingrese el segundo numero: "))
    time.sleep(1)

else:
    print("Estos son los numeros: ",num1,num2)

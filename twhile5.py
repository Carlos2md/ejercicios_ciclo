import time
num1=int(input("Por favor ingrese un numero: "))
num2=int(input("Por favor ingrese un numero mayor que "+str(num1)+": "))


while num2>num1: 
    num1=num2
    num2=int(input(f"Ingrese un numero mayor que {num1}: "))
else:
    print(f"{num2} no es mayor que {num1}")
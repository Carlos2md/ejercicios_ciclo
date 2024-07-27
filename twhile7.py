import time
num_impar=int(input("Por favor ingrese un numero: "))

flag=True
while flag:
    par_impar=num_impar%2 #usar modulo
    if par_impar==0:
     num_impar=int(input("Por favor ingrese un numero: "))   
    else:
       flag=False

else:
    print(f"El numero impar es {num_impar}")

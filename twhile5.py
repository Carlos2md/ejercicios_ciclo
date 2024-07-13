import time
num1=int(input("Por favor ingrese un numero: "))
num2=int(input("Por favor ingrese un numero mayor que "+str(num1)+": "))
num3=0
##if num2<=num1:
  ##  print(num2,"no es mayor",num1)
##else:
  ##  while (num2>num1):
    ##    num2=int(input("Por favor ingrese un numero mayor que "+str(num2)+": "))
      ##  time.sleep(1)
    ##else:
      ##  print(num2,"no es mayor a",num3)
while num2<=num1:
    print(num2,"no es mayor a",num1)
    break
else:
   ## num1=num3
    while num2>num1:
        num1=int(input("Por favor ingrese un numero mayor que "+str(num2)+": "))
     ##   num3=num2
        time.sleep(1)

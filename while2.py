import time
i=0

while i<=10:
    print(i)
    i=i+1
    time.sleep(1)

    break
else:
    print("Hemos terminado el ciclo")
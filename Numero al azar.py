from random import *
x = randrange(1,10)
cont = 0
y = 0

while (x != y):
 y = int(input("Digite un numero entre 1 y 10: "))
 if(y > x):
    print("Ingrese un numero menor")
 elif(y < x):
    print("Ingrese un numero mayor")
cont += 1

print("Felicidades")
print ("Tu numero de intentos fue " + str(cont))

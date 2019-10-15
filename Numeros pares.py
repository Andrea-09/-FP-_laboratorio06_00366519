x = 1
S = 0
N = 0
cont = 0

while x != 0:
    x = int(input("Digite un numero par: "))
    print("¿Desea digitar otro numero par?")
    y = input("")
    if y == 'S':
        print("Digite un numero par")
    elif y == 'N':
        print("Felicidades")
       
cont += 1
print("Tu numero de intentos fue " + str(cont))

comprobar = True
while comprobar == True:
    n = int(input("Ingrese un numero entero positivo: "))
    if n > 0:
        i = 1
        while i < 11:
            print(n, "por", i, "es igual a:", n*i)
            i += 1
            
        comprobar = False
    else:
        print("Ingrese un numero entero psotivo. Inténtelo de nuevo")

saldo= 1000
cont=0

while True:
    print ("Que operacion desea utilizar?:")
    print ("1.- Retirar")
    print ("2.- Deposito")
    print ("0.- Para cerrar")
    opcion=int(input("Ingrese opcion:"))
    if opcion==1:
        monto=int(input("Ingrese monto a retirar:"))    
        saldo=saldo-monto
        print ("Ha retirado " , monto)
        print ("Su saldo es " + str(saldo))
    elif opcion==2:
        monto=int(input("Ingrese monto a Depositar:"))          
        saldo=saldo+monto
        print ("Su nuevo saldo es", saldo)
    
    elif opcion==0:
        break

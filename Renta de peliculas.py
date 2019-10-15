def precio_final():
    '''Funcion para mostrar el valor final'''
    x=int(input("Ingrese el valor de la primera pelicula"))
    y=int(input("Ingrese el valor de la segunda pelicula"))
    z=int(input("Ingrese el valor de la tercera pelicula"))
    
    if (x<y and x>z):
        print("El precio final es: " +str(x+y) + "\n")
    elif (y>x and y<z):
        print("El precio final es: " +str(y+z) + "\n")
    elif (z<x and z>y):
        print("El precio final es: " +str(z+x) + "\n")
    else:
        print("Adios" + "\n")       

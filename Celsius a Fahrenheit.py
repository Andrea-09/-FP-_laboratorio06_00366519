def fahrenheit_celsius():
    '''convierte temperatura en grados fahrenheit a grados celsius'''
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)

def celsius_fahrenheit():
    '''convierte temperatura en grados celsius a fahrenheit'''
    celsius = int(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius +32
    return '{} grados Celsius son {} grados Fahrenheit'.format(celsius, fahrenheit)

def celsius_Kelvin ():
    '''convierte grados celsius a kelvin'''
    celsius = int(input("Ingrese la temperatura en grados celsius: ")
    Kelvin = celsius + 273
    return '{} grados Celsius son {} grados Kelvin'.format(celsius, kelvin)

def kelvin_celsius ():
    '''Convierte kelvin a grados celsius'''
    Kelvin = int(input("Ingrese la temperatura en kelvin: ")
    celsius = kelvin + 273
    return '{} grados Kelvin son {} grados Celsius'.format(kelvin, celsius)
                    

while True:
    print("1.- Fahrenheit a Celsius")
    print("2.- Celsius a Fahrenheit")
    print("3.- Celsius a Kelvin")
    print("4.- Kelvin a Celsius")

    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print(celsius_kelvin())
        else:
            print('Hasta luego')
        

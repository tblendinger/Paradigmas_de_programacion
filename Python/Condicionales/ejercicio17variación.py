#tratamiento de excepciones tryexcept
#while para error de numero negativo

try:
    n = int(input("Ingrese un número "))

    while n < 0:
        print("Error")
        n = int(input("Ingrese un número positivo "))

    if n < 100:
        if n < 10:
           print("El numero tiene 1 cifra")
        else:
           print("El numero tiene 2 cifras")
    else:
        if n < 1000:
            print("El número tiene 3 cifras")
        else: 
            print("Error, el número tiene más de 3 cifras")
            
except ValueError:
    n = int(input("Ingrese un caracter válido "))                           
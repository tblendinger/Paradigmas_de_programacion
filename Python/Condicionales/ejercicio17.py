#confexionar un programa que permita cargar un numero entero positivo de hasta 3 cifras que muestre un mensaje si 
# tiene 1, 2 o 3 cifras. mostrar error si el numero tiene más de 3 cifras.

n = int(input("Ingrese un número "))

if n < 0: 
    print("Error, ingrese un número positivo")
else:
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

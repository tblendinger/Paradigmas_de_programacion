#Se ingresan 3 números, si al menos uno de ellos es menos a 10, mostrar mensaje "Menor a 10"

n1 = int(input("Ingrese el primer numero "))
n2 = int(input("Ingrese el segundo numero "))
n3 = int(input("Ingrese el tercer numero ")) 

if (n1 or n2 or n3) < 10:
    print("Hay un numero menor a 10")
else:
    print("Son mayores a 10")
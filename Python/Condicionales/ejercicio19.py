#Compuertas de flujo
#identificar de 3 numeros que se ingresan cual es el mayor de los 3      

n1 = int(input("Ingrese el primer numero "))
n2 = int(input("Ingrese el segundo numero "))
n3 = int(input("Ingrese el tercer numero "))        

if n1 > n2 and n1 > n3:
    print( n1 , " es el mayor")
elif n2 > n3:
    print( n2 , "es el mayor")
elif n3 > n2: 
    print( n3 , "es el mayor")
else:
    print("Los tres números son iguales")
                                                                                        
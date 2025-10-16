#Ingresar 3 notas, calcular el promedio y mostrar promocionado si es mas de 7, regular mayor o igual a 4 y desaprobado menor a 4

import math

nota1 = int(input("Ingrese la nota de matemáticas "))
nota2 = int(input("Ingrese la nota de física "))
nota3 = int(input("Ingrese la nota de biología "))

prom = (nota1 + nota2 + nota3)/3


if prom >= 7:
    print("Promocionado con " , math.ceil(prom))
elif prom >= 4:
    print("Regular con " , prom)
else: 
    print("Desaprobado")
    

nota1 = int(input("Ingrese la nota de matemáticas "))
nota2 = int(input("Ingrese la nota de física "))
nota3 = int(input("Ingrese la nota de biología "))

if ((nota1 + nota2 + nota3) / 3 >= 7): 
    print("Promocionado")
else:
    print("No Promocionado")
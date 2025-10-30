# Solicitar la carga del nombre en minúscula, mostrar un mensaje si dicho nombre empieza con vocal
nombre = input("Ingrese un nombre: ")

if nombre[0] == ("a" or "e" or "i" or "o" or "u"):
    print("El nombre empieza con vocal")
else:
    print("El nombre empieza con consonante")
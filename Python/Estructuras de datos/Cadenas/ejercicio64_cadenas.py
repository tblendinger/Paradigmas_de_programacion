#64: ingresar un mail por teclado y validar si el str ingresado contiene un solo caracter @

mail = input("Ingrese una dirección de mail: ")

contador = 0
for caracter in mail:
    if caracter == "@":
        contador += 1

if contador == 1:
    print("La dirección es válida")
else:
    print("La dirección no es válida")
        


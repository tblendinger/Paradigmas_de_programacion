#68 Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el str ingresado tenga entre
# 10 y 20 caracteres para que sea válido. Caso contrario mostrar mensaje de error.

clave = input("Ingrese una clave de entre 10 y 20 caracteres: ")

if  10 <= len(clave) <=20:
    print("La clave es válida")
else:
    print("Error")

#Realizazar la carga de un nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen

nombre = input("Ingrese un nombre ") 
caract1=nombre[0]
caractul=nombre[-1]
cant=len(nombre)
print("Primer caracter: ",caract1, "Ultimo caracter: ", caractul, "cantidad de letras: ", cant)
for i in nombre:
    print(i)
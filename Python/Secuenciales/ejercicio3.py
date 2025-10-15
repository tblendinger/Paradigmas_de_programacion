#Realizar un cálculo de un producto ingresando precio y cantidad del mismo, mostrando precio y total a pagar
precio_prod = int(input("Ingresar el precio del producto "))
cantidad = int(input("Ingresar la cantidad "))
total = precio_prod * cantidad
print("El precio unitario es $" , precio_prod , ", y el valor total es $" , total)
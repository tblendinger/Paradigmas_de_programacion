# 80 Crear y cargar una lista con 5 enteros.
# implementar un algoritmo que identifique el mayor valor de la lista.

lista = []
for i in range (5):
    num=int(input(" Carga el numero :"))
    lista.append(num)


aux=lista[0]
for i in range (1,5):
    if lista[i]>aux:
        aux=lista[i] 
print(lista)
print(aux)
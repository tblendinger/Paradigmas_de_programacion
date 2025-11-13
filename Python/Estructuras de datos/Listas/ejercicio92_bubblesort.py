# 92: Cargar una lista con 5 elementos enteros.
# Ordenarla de menor a mayor y mostrarla por pantalla.
# luego ordenar de mayor a menor e imprimir nuevamente.

lista = []
for x in range (5):
    num=int(input(" Carga el numero :"))
    lista.append(num)

n = len(lista)

for i in range(1,n):
    for j in range(0,n-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]  
            lista[j] = lista[j+1]
            lista[j+1] = aux
            
print(lista)

for i in range(1,n):
    for j in range(0,n-1):
        if lista[j] < lista[j+1]:
            aux = lista[j]  
            lista[j] = lista[j+1]
            lista[j+1] = aux
            
print(lista)


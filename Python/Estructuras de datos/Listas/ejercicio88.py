# 88: Se debe crear y cargar una lista donde almacenar 5 sueldos.
# Desplazar el valor mayor de la lista a la última posición

lista = []
for i in range (5):
    num=int(input(" Carga el numero :"))
    lista.append(num)
print("Antes: " , lista)

n = len(lista)

mayor=lista[0]
idx = 0
for i in range (1,n):
    if lista[i]>mayor:
        mayor=lista[i] 
        idx = i
print(mayor)


for i in range(idx, n-1):
    lista[i] = lista[i+1]
        
lista[-1] = mayor
        
print("Después: ", lista)


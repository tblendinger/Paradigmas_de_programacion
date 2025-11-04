#Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 caracteres o más

lista = ["Tomas" , "Benjamin" , "Marcos" , "Tobias" , "Ana"]

contador = 0

for i in lista:
    if len(i) >= 5:
        contador = contador + 1
        
print("La cantidad de nombres con 5 o más letras es " , contador)
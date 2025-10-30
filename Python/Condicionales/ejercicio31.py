#Una planta que fabrica perfiles de hierro posee un lote de n piezas. 
#Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar, 
#y luego ingrese la longitud de cada perfil.
#Sabiendo que la pieza cuya longitud esta comprendida entre 1.20 y 1.30 metros es considerada apta, 
#imprimir por pantalla la cantidad de piezas aptas que hay por lote.

n = int(input("Ingrese la cantidad de piezas del lote: ")) 

perfiles_aptos = 0
for i in range (1 , n+1):
    longitud = int(input(f"Ingrese la longitud del perfil {i}: ")) 
    
    if  longitud <= 130 and  longitud >= 120:
        perfiles_aptos += 1


print("Hay ", perfiles_aptos  , "piezas aptas en el lote")
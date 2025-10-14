#Verificar sueldo ingresado, si supera los 3000 paga impuestos

sueldo = int(input("Ingresar sueldo: "))

if sueldo > 3000:
    print("Paga impuestos")
else: 
    print("No paga impuestos")
#En una empresa trabajan n empleados, cuyos sueldos oscilan entre 100 y 500.
#Realizar un programa que lea los sueldos que cobra cada empleado e informe cuantos cobran entre 100 y 300 y cuantos cobran más de 300.
#Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

cant_empleados = int(input("Ingrese la cantidad de empleados de la empresa: "))

sueldototal=0
empleadosA = 0
empleadosB = 0
for i in range (1, cant_empleados+1): 
   
    sueldo = int(input(f"Ingrese el sueldo del empleado {i}: "))

    if  100 <= sueldo <= 300:
        empleadosA += 1
    
    elif sueldo > 300:
        empleadosB += 1
    sueldototal+=sueldo

print(empleadosA, "Cobran entre 100 y 300, y " , empleadosB , "Cobran más de 300")
print("El gasto total de la empresa en sueldos es: ", sueldototal)
    
    
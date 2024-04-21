# Título: TP00-02 - ASIENTOS DE CONFERENCIA
# Fecha: 03-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
#     Realizar un programa que permita ingresar la cantidad de inscriptos a una conferencia y la cantidad de asientos disponibles en el auditorio.
#     Se debe indicar si alcanzan los asientos. Si los asientos no alcanzan, indicar cuantos faltan para que todos los inscriptos puedan sentarse

import random

cantAsTot = 250

cantDeInscriptos = int(input("Ingresa la cantidad de inscriptos para la conferencia: "))
while cantDeInscriptos < 0:
    cantDeInscriptos = int(input("Ingresa la cantidad de inscriptos para la conferencia: "))

cantAsDisp = cantAsTot - cantDeInscriptos


if cantDeInscriptos > cantAsTot:
    faltan = cantDeInscriptos - cantAsTot
    print("¡Faltan", faltan,"asientos!")
elif cantDeInscriptos == cantAsTot:    
    print("¡La cantidad de asientos alcanza perfecto!")
else:
    sobran = cantAsTot - cantDeInscriptos
    print("Sobran", sobran,"asientos!")


    
        



# Título: TP00-02 - PROMEDIO DE TEMPERATURAS
# Fecha: 28-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Realizar un programa que solicite la carga de las temperaturas de todos los días de enero y al finalizar devuelva la 
# temperatura promedio, máxima y mínima del mes. 

eneroTemps = []
for i in range(1,10,1):
    tempActual = int(input("Ingrese la temp de hoy: "))
    eneroTemps.append(tempActual)

print("Temp minima del mes", min(eneroTemps))

print("Temp max del mes", max(eneroTemps))

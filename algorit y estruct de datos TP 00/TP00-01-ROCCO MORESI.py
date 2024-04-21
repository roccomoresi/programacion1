# Título: TP00-01 - AUTONOMÍA DE VEHÍCULO
# Fecha: 03-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Calcula cuantos kilómetros puede recorrer un vehículo según la cantidad de litros de combustible
# ingresados y el tipo de camino

litrosCombustible = int(input("Ingresa la cantidad de litros de combustible: "))
tipoCamino = input("Ingresa el tipo de camino [r=ruta, c=ciudad]: ")

if tipoCamino == "r":
    autonomia = litrosCombustible * 14.1
else:
    autonomia = litrosCombustible * 10.3
    
print()
print("La autonomía es de " + str(autonomia) + " kilómetros")
# Título: TP00-01 - AUTONOMÍA DE VEHÍCULO
# Fecha: 03-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar un programa que pida uno por 
# uno los precios de los productos comprados por el cliente, y que al ingresar un precio igual a cero muestre el total que 
# debe abonar por la compra y la cantidad de productos comprados. 

import random 

def busqueda(lista, valorB):
    pos = -1
    i = 0
    while pos == -1 and i<len(lista):
        if lista[i] == valorB:
            pos = i
        i+=1
    return pos





precioDeProductos = []
suma = 0

precio = int(input("Ingresa el precio que corresponda a tu producto: "))
while precio != 0:
    precioDeProductos.append(precio)
    suma += precio
    precio = int(input("Ingresa el precio que corresponda a tu producto: "))



print("La suma es", suma)

print("La cantidad de prods es", len(precioDeProductos))
        





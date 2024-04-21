# Título: TP00-07 - FORMAS DE PAGO 
# Fecha: 28-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas 
# las opciones de pago disponibles (si es en cuotas además del precio final debe mostrar el valor de cada cuota). Los 
# descuentos o recargos según las formas de pago son los siguientes: 
# En efectivo aplicar 10% de descuento 
# Tarjeta 1 pago mantener el precio de lista 
# Tarjeta 3 pagos recargar 5% 
# Tarjeta 6 pagos recargar 10% 
# Tarjeta 12 pagos recargar 15% 
# Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio 
# de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el 
# input dos veces.

import random


formasDePago = ["efectivo", "Tarjeta1", "Tarjeta3", "Tarjeta6", "Tarjeta12"]


precioTotal = 100

pagoDelCliente = int(input("Ingrese la forma de pago. (1 efectivo),(2 Tarjeta1), (3 Tarjeta3), (4 Tarjeta 6), (5 Tarjeta12): "))



if pagoDelCliente == 1:
    precioTotal = precioTotal - precioTotal * 10/100
if pagoDelCliente == 2:
    precioTotal = precioTotal + precioTotal * 5/100
if pagoDelCliente == 3:
    precioTotal = precioTotal + precioTotal * 10/100
if pagoDelCliente == 4:
    precioTotal = precioTotal + precioTotal * 15/100

print("El precio total seria", precioTotal)


 





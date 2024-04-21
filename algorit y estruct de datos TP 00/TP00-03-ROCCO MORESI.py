# Título: TP00-03 - COBRO Y VUELTO
# Fecha: 03-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Escribir un programa basico de caja, donde se ingrese el precio total de la compra, luego se ingrese el monto con el cual el cliente
# abona la compra, y finalmente informe con un mensaje si no es suficiente con lo que abono o, caso contrario, informe el vuelto que se le debe
# dar al cliente.

import random

montoTotalCompra = int(input("Ingrese el precio total de la compra: "))

while montoTotalCompra < 0:
    montoTotalCompra = int(input("Ingrese el precio total de la compra: "))
    

montoCliente = int(input("Ingrese el monto con el que abona el cliente: "))
while montoCliente < 0:
    montoCliente = int(input("Ingrese el monto con el que abona el cliente: "))


if montoCliente < montoTotalCompra:
    faltan = montoTotalCompra - montoCliente
    print("¡Faltan $",faltan,"por abonar!")
elif montoCliente > montoTotalCompra:
    vuelto = montoCliente - montoTotalCompra
    print("El vuelto que le corresponde al cliente serian: $",vuelto)
else:
    print("Entregar productos.")



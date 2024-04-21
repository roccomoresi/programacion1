# Título: TP01-03 -  GASTO DE TRANSPORTE SUBTE
# Fecha: 31-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que 
# dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita 
# desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el 
# total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función. 
# Cantidad de viajes 
# 1 a 20 
# Valor de 1 pasaje 
# Averiguar en internet el valor actualizado 
# 21 a 30 
# 20% de descuento 
# 30% de descuento 
# 31 a 40 
# 41 o más 
# 40% de descuento



def viajesDeEsteMes(cant):
    if cant >= 1 and cant <= 20:
      valorPasaje = 602
    elif cant >= 21 and cant <= 30:
        valorPasaje = 602 - 602 * 20/100
    elif cant >= 31 and cant <= 40:
        valorPasaje = 602 - 602 * 30/100
    elif cant >= 41:
        valorPasaje = 602 - 602 * 40/100
    else:
        print("VALOR INVALIDO!")
    return valorPasaje

cantidadDeViajes = int(input("Ingrese la cantidad de viajes por mes que hace en subte: "))

dineroPorMesSubte = int(viajesDeEsteMes(cantidadDeViajes))

print("Pagara",dineroPorMesSubte,"por mes.")

    
# Título: TP00-04 - AUMENTO DE LIMITES DE TARJETAS
# Fecha: 03-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 
# 2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo aumentarán un 50%. Desarrollar un 
# algoritmo para calcular el nuevo límite según el límite actual y el tipo de tarjeta del cliente.

unoActual= 1500

dosActual= 2000

tresActual= 4000

cuatroActual = 10000

cincoActual = 20000

seisActual = 50000

numDeTarjeta  = int(input("Ingrese el tipo de tarjeta que tiene. 1,2,3,4,5,6: ") )

while numDeTarjeta <= 0 or numDeTarjeta > 6:
    numDeTarjeta  = int(input("Ingrese un tipo de tarjeta VALIDO ----> 1,2,3,4,5,6: ") )
    
if numDeTarjeta == 1:
    nuevoValor = int(unoActual * 0.25 + unoActual)
elif numDeTarjeta == 2:
    nuevoValor = int(dosActual * 0.35 + dosActual)
elif numDeTarjeta == 3:
    nuevoValor = int(tresActual * 0.40 + tresActual)
elif numDeTarjeta == 4:
    nuevoValor = int(cuatroActual * 0.50 + cuatroActual)
elif numDeTarjeta == 5:
    nuevoValor = int(cincoActual * 0.50 + cincoActual)
else:
    nuevoValor = int(seisActual * 0.50 + seisActual)
    
        
    
print("Su limite de tarjeta actualizado es", nuevoValor)
    






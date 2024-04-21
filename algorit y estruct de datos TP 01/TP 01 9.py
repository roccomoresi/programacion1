# Título: TP01-09 -     CAJONES DE NARANJAS 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Resolver el siguiente problema utilizando funciones: Un productor frutihortícola desea contabilizar sus cajones de 
# naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada uno puede 
# transportar hasta media tonelada (500 kilogramos). En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos 
# cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. Se 
# solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden 
# llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. 
# Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.  
# Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del 
# camión no debe ser inferior al 80%; en caso contrario el camión no será despachado por su alto costo.

import random

import random

def naranjasPorCajon(cant, jugo, pesoTotal, cajones, otroReparto):
    i = 0
    for cantidad in range(cant):
        peso = random.randint(150, 350)
        while i <= 100:
            if peso < 200 or peso > 300:
                jugo += 1
            i += 1
        else:  
            cajones += 1
            pesoTotal += peso
    if cant > 100:
        otroReparto = cant - 100
    
    return cajones, jugo, otroReparto


# PROG PRINCIPAL

jugo = 0
pesoTotal = 0
cajones = 0
otroReparto = 0


cant = int(input("Ingrese la cant de naranjas cosechadas: "))

info = naranjasPorCajon(cant,jugo, pesoTotal, cajones, otroReparto)

print(info)
            
    
    
        

            
            
    
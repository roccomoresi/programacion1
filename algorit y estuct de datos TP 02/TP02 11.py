# Título: TP02-11 -        AZAR Y ELEMENTOS IMPARES   

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean 
# impares. Imprimir las dos listas por pantalla. 
# • Programa TP02-11A: El proceso deberá realizarse utilizando listas por comprensión. 
# • Programa TP02-11B: El proceso deberá realizarse utilizando la función incorporada filter(). (investigarla) 

import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(10)] 
print("Lista de números aleatorios:", numeros_aleatorios)

numeros_impares = [numero for numero in numeros_aleatorios if numero % 2 != 0]
print("Lista de números impares:", numeros_impares)

numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]  
print("Lista de números aleatorios:", numeros_aleatorios)

numeros_impares = list(filter(lambda x: x % 2 != 0, numeros_aleatorios))
print("Lista de números impares:", numeros_impares)

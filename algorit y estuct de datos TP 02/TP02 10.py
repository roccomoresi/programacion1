# Título: TP02-10 -        ELEMENTOS IMPARES   

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 
# 100 y 200. 

numeros_impares = [numero for numero in range(100, 201) if numero % 2 != 0]
print(numeros_impares)

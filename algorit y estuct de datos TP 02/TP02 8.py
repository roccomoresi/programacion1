# Título: TP02-08 -        LISTA NORMALIZADA 

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus 
# elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar 
# también un programa que permita verificar el comportamiento de la función. Por ejemplo, normalizar([1, 1, 2]) debe 
# devolver [0.25, 0.25, 0.50]. 

def normalizar(lista):
    suma_total = sum(lista)
    
    proporciones = [elemento / suma_total for elemento in lista]
    
    return proporciones

lista_original = [1, 1, 2]
lista_normalizada = normalizar(lista_original)
print("Lista original:", lista_original)
print("Lista normalizada:", lista_normalizada)

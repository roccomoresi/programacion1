# Título: TP02-06 -        ELEMENTOS ELIMINADOS 

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. Imprimir la lista 
# original, la lista de valores a eliminar y la lista resultante. La función deben modificar la lista original sin crear una copia 
# modificada. 


def eliminar_valores(lista_original, lista_a_eliminar):
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar:", lista_a_eliminar)
    
    
    lista_resultante = [elemento for elemento in lista_original if elemento not in lista_a_eliminar]
    
    print("Lista resultante:", lista_resultante)

lista_original = [1, 2, 3, 4, 5, 6, 7]
lista_a_eliminar = [2, 4, 6]

eliminar_valores(lista_original, lista_a_eliminar)

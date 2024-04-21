# Título: TP02-04 -       ELEMENTOS REPETIDOS

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribir funciones para:
# a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.
# b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no
# debe modificar la lista.
# c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin
# importar el orden.
# Combinar estas tres funciones en un mismo programa.

import random

def listaAleatoria(lista, cant):
    for i in range(cant):
        num = random.randint(1, 100)
        lista.append(num)
    return lista

def repetidos(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def unicos(lista):
    lista2 = []
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2.append(lista[i])
    return lista2

lista = []

n = int(input("Ingrese cantidad de numeros en la lista que desea: "))
listaHecha = listaAleatoria(lista,n)
resu = repetidos(listaHecha)
listaUnicos = unicos(listaHecha)

print(listaHecha)
print(resu)
print(listaUnicos)
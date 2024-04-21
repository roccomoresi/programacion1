# Título: TP02-03 -      ELEMENTOS NUMÉRICOS
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento,
# imprimiendo lo que devuelve cada función luego de invocar a cada una de ellas:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar
# de dos dígitos.
# b. Calcular y devolver el producto de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la
# función lo recibe como parámetro. No utilizar listas auxiliares.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa
# es [50, 17, 91, 17, 50].


import random

def cargarNums(lista):
    cantNums = random.randint(10, 99)
    for i in range(cantNums):
        num = random.randint(1000, 9999)
        lista.append(num)
    return lista

def eliminarValor(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1

def esCapicua(lista):
    inicio = 0
    fin = len(lista) - 1
    while inicio < fin:
        if lista[inicio] != lista[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


numeros = []
listaHecha = cargarNums(numeros)
print("Lista original:", listaHecha)

valor_eliminar = int(input("Ingrese el valor a eliminar: "))
eliminarValor(listaHecha, valor_eliminar)
print("Lista después de eliminar el valor:", listaHecha)

if esCapicua(listaHecha):
    print("La lista es capicúa.")
else:
    print("La lista no es capicúa.")


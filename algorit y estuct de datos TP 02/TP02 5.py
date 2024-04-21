# Título: TP02-05 -       ELEMENTOS AL CUADRADO

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
# Luego se solicita imprimir los últimos 10 valores de la lista.

def cuadrados(lista, n):
    cuadradoDeUno = 1 ** 2
    cuadradoDeN = n ** 2
    lista.append(cuadradoDeUno)
    for i in range(2, n + 1):  
        lista.append(i ** 2)
    return lista

def ultimosDiez(lista):
    if len(lista) <= 10:
        return lista
    else:
        return lista[-10:]

lista = []

n = int(input("Ingrese un número entero mayor que 1: "))

listaHecha = cuadrados(lista, n)

print("Lista completa de cuadrados:", listaHecha)

ultimos_10 = ultimosDiez(listaHecha)
print("Los últimos 10 valores de la lista son:", ultimos_10)


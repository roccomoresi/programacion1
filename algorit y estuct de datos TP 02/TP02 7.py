# Título: TP02-07 -        VERIFICAR ORDEN DE ELEMENTOS 

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente 
# o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
# además un programa para verificar el comportamiento de la función.  

def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


lista1 = [1, 2, 3]
lista2 = ['b', 'a']
lista3 = [5, 3, 7, 8]


print("¿La lista 1 está ordenada?", ordenada(lista1))
print("¿La lista 2 está ordenada?", ordenada(lista2))
print("¿La lista 3 está ordenada?", ordenada(lista3))


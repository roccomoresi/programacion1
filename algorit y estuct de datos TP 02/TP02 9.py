# Título: TP02-09 -        INTERCALACIÓN DE ELEMENTOS  

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Intercalar los elementos de una lista entre los elementos de otra. La intercalación podrá realizarse utilizando el método 
# insert o mediante la técnica de rebanadas (slicing), y nunca se creará una lista nueva, sino que se modificará la primera. 
# Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden tener 
# distintas longitudes. 

def intercalar_con_insert(lista1, lista2):
    index = 1
    
    for elemento in lista2:
        lista1.insert(index, elemento)
        index += 2


lista1 = [8, 1, 3]
lista2 = [5, 9, 7]
intercalar_con_insert(lista1, lista2)
print("Lista 1 intercalada:", lista1)

def intercalar_con_slicing(lista1, lista2):
    index = 1
    
    for elemento in lista2:
        lista1[index:index] = [elemento]
        index += 2

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]
intercalar_con_slicing(lista1, lista2)
print("Lista 1 intercalada:", lista1)


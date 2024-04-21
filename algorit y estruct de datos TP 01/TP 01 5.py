# Título: TP01-05 -   OBLONGOS Y TRIANGULARES 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción: Escribir dos funciones separadas que reciban un número natural y devuelvan verdadero o falso según el número sea de 
# alguna de las siguientes categorías: 
# Función oblongo(): Informa si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
# multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3. 
# Función triangular(): Informa si un número es triangular. Un número se define como triangular si puede expresarse 
# como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número 
# triangular porque se obtiene sumando 1+2+3+4.
# Opcional: Desarrollar estas funciones pero bajo la forma de funciones lambda.
import random



def oblongo(numero):
    for i in range(numero):
        if i * (i+1) == numero:
            return True
    return False


def triangular():
    return


numero = int(random.randint(1, 100))
print(numero)
    

respuesta = oblongo(numero)

print(respuesta)
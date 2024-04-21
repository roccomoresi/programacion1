# Título: TP01-01 - MAYOR ENTRE TRES NÚMEROS
# Fecha: 29-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor
# estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
# también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje
# informativo si éste no existe.

def mayor_entre_tres(num1, num2, num3):
    mayorEstricto = -1
    if num1 > num2:
        if num1 > num3:
            mayorEstricto = num1
            
    if num2 > num1:
        if num2 > num3:
            mayorEstricto = num2

    if num3 > num1:
        if num3 > num2:
            mayorEstricto = num3

    return mayorEstricto


num1 = int(input("numero 1: "))

num2 = int(input("numero 2: "))

num3 = int(input("numero 3: "))

pedo = mayor_entre_tres(num1,num2,num3)

print(pedo)
            
    

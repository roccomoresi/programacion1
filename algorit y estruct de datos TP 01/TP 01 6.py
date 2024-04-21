# Título: TP01-05 -    CONCATENAR BÁSICO  
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de 
# concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades 
# de Python no vistas en clase, ni tampoco concatenar strings mediante la conversión de número a cadena. 

import random

def dosNumConcatenados(num1,num2):
    digitos_num2 = 0
    temp_num2 = num2
    while temp_num2 > 0:
        temp_num2 //= 10
        digitos_num2 += 1
    resultado = num1 * (10 ** digitos_num2) + num2
    return resultado

num1 = random.randint(1,1000000)
num2 = random.randint(1,1000000)
print(num1)
print(num2)
resu = dosNumConcatenados(num1,num2)
print(resu)

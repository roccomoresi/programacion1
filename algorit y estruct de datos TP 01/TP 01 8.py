# Título: TP01-08 -    DÍA SIGUIENTE 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma 
# de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa 
# para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes y año cualquiera basándose en 
# la función suministrada. Considerar que la semana comienza en domingo.

import random

def diaDeLaSem(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año//100
    año2 = año % 100
    diaSem = (((26* mes -1) // 10) + dia + año2 + (año2 // 4) -(2 * siglo)) % 7
    if diaSem < 0:
        diaSem = diaSem + 7
    return diaSem


def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def imprimir_dias(dias_del_mes):
    print(dias_del_mes)
    mostrar = 0  
    for i in range(dias_del_mes):
        if mostrar <= 6:
            print(mostrar, end=" ")
            mostrar += 1
        else:
            mostrar = 0
            print(mostrar, end=" ")
            mostrar += 1
    print()  
    return



#PROGRAMA DE LA SOLUCION 



año = random.randint(1900, 2023)
mes = random.randint(1, 12)
dia = random.randint(1, 31)
print("Fecha aleatoria:", dia, "-", mes, "-", año)
#averiguo si es bisiesto

if es_bisiesto(año):
    print("El año es bisiesto.")
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    print("El año no es bisiesto.")
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cant_dias_mes = (dias_por_mes[mes])
print(cant_dias_mes)

# Imprimir los días del mes
imprimir_dias(dias_por_mes[mes])





            
        
        
        



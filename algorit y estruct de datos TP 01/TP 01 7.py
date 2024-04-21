# Título: TP01-05 -    DÍA SIGUIENTE 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribir una función diaSiguiente() que reciba como parámetro una fecha cualquiera expresada por tres enteros 
# (correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando 
# esta misma función, sin modificaciones ni agregados, desarrollar programas que permitan: 
# • Programa TP01-07A: Sumar N días a una fecha. 
# • Programa TP01-07B: Calcular la cantidad de días existentes entre dos fechas cualesquiera.

def diaSiguiente(dia, mes, año):
    es_bisiesto = False
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        es_bisiesto = True
        dias_por_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        es_bisiesto = False
        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
    if dia >= 1 and dia <= dias_por_mes[mes]:
        dia += 1
        if dia > dias_por_mes[mes]:
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                año += 1
        return dia, mes, año
    else:
        return None  

result = diaSiguiente(28, 2, 2006)

print(result)

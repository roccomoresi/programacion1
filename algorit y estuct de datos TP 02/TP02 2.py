# Título: TP02-02 -      MES NÚMERO A TEXTO 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes.
# Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la
# función con dicho número como argumento, y finalmente un print de lo que la función devuelve.

def mesNum(num):
    
    if num == 1:
        mes = "enero"
    elif num == 2:
        mes = "febrero"
    elif num == 3:
        mes = "marzo"
    elif num == 4:
        mes = "abril"
    elif num == 5:
        mes = "mayo"
    elif num == 6:
        mes = "junio"
    elif num == 7:
        mes = "julio"
    elif num== 8:
        mes = "agosto"
    elif num == 9:
        mes = "septiembre"
    elif num == 10:
        mes = "octubre"
    elif num == 11:
        mes = "noviembre"
    elif num == 12:
        mes = "diciembre"
    else:
        mes = "Número de mes no válido"
    
    return mes

num = int(input("Ingrese el numero de mes: "))
mes = mesNum(num)
print(mes)




# Título: TP01-02 - FECHA VÁLIDA
# Fecha: 29-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes y año de una fecha, y
# verifique si corresponden a una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años
# bisiestos. La función debe devolver True o False según la fecha sea correcta o no. Realizar también un programa para
# verificar el comportamiento de la función.

def fechaValida(dia, mes, año, valido):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):

        if (mes == 1 and dia > 0 and dia < 32):
            valido = True
        else:
            valido = False

            if (mes == 2 and dia > 0 and dia < 30):
                valido = True
            else:
                valido = False

                if (mes == 3 and dia > 0 and dia < 32):
                    valido = True
                else:
                    valido = False
        
                    if (mes == 4 and dia > 0 and dia < 31):
                        valido = True
                    else:
                        valido = False

                        if (mes == 5 and dia > 0 and dia < 32):
                            valido = True
                        else:
                            valido = False

                            if (mes == 6 and dia > 0 and dia < 31):
                                valido = True
                            else:
                                valido = False
        
                                if (mes == 7 and dia > 0 and dia < 32):
                                    valido = True
                                else:
                                    valido = False
        
                                    if (mes == 8 and dia > 0 and dia < 32):
                                        valido = True
                                    else:
                                        valido = False
        
                                        if (mes == 9 and dia > 0 and dia < 31):
                                            valido = True
                                        else:
                                            valido = False

                                            if (mes == 10 and dia > 0 and dia < 32):
                                                valido = True
                                            else:
                                                valido = False
        
                                                if (mes == 11 and dia > 0 and dia < 31):
                                                    valido = True
                                                else:
                                                    valido = False
                
                                                    if (mes == 12 and dia > 0 and dia < 32):
                                                        valido = True
                                                    else:
                                                        valido = False


    else:
        if (mes == 1 and dia > 0 and dia < 32):
            valido = True
        else:
            valido = False

            if (mes == 2 and dia > 0 and dia < 29):
                valido = True
            else:
                valido = False

                if (mes == 3 and dia > 0 and dia < 32):
                    valido = True
                else:
                    valido = False
        
                    if (mes == 4 and dia > 0 and dia < 31):
                        valido = True
                    else:
                        valido = False

                        if (mes == 5 and dia > 0 and dia < 32):
                            valido = True
                        else:
                            valido = False

                            if (mes == 6 and dia > 0 and dia < 31):
                                valido = True
                            else:
                                valido = False
        
                                if (mes == 7 and dia > 0 and dia < 32):
                                    valido = True
                                else:
                                    valido = False
        
                                    if (mes == 8 and dia > 0 and dia < 32):
                                        valido = True
                                    else:
                                        valido = False
        
                                        if (mes == 9 and dia > 0 and dia < 31):
                                            valido = True
                                        else:
                                            valido = False

                                            if (mes == 10 and dia > 0 and dia < 32):
                                                valido = True
                                            else:
                                                valido = False
        
                                                if (mes == 11 and dia > 0 and dia < 31):
                                                    valido = True
                                                else:
                                                    valido = False
                
                                                    if (mes == 12 and dia > 0 and dia < 32):
                                                        valido = True
                                                    else:
                                                        valido = False
    return valido

    

año = int(input("Ingresa año: "))

mes = int(input("Ingresa mes: "))

dia = int(input("Ingresa dia: "))

xd = True



esONoValido = fechaValida(dia, mes, año, xd)

print(esONoValido)
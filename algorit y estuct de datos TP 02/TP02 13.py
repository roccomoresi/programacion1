# Título: TP02-13 -     REGISTRO DE VISITAS DE SOCIOS    

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Resolver el siguiente problema, utilizando funciones:  
# Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco 
# dígitos hasta ingresar un cero como fin de carga. 
# Se solicita: 
# a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe). 
# b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de 
# entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron. 

def registrar_ingresos():
    registros = []
    while True:
        numero_socio = int(input("Ingrese el número de socio (0 para finalizar): "))
        if numero_socio == 0:
            break
        registros.append(numero_socio)
    return registros

def contar_ingresos(registros):
    conteo_ingresos = {}
    for numero_socio in registros:
        conteo_ingresos[numero_socio] = conteo_ingresos.get(numero_socio, 0) + 1
    return conteo_ingresos

def dar_de_baja(registros, numero_socio_baja):
    ingresos_eliminados = registros.count(numero_socio_baja)
    registros = [registro for registro in registros if registro != numero_socio_baja]
    return registros, ingresos_eliminados

def mostrar_registros(registros):
    print("Registros de entrada al club:")
    for registro in registros:
        print(registro)

registros = registrar_ingresos()

conteo_ingresos = contar_ingresos(registros)
print("Ingresos de cada socio:")
for numero_socio, ingresos in conteo_ingresos.items():
    print("Socio", numero_socio, "- Ingresos:", ingresos)

numero_socio_baja = int(input("Ingrese el número de socio dado de baja: "))

registros, ingresos_eliminados = dar_de_baja(registros, numero_socio_baja)

print("\nRegistros de entrada antes de dar de baja al socio:")
mostrar_registros(registros)
print("\nSe eliminaron", ingresos_eliminados, "ingresos del socio", numero_socio_baja)

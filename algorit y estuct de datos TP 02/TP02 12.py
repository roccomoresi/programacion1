# Título: TP02-12 -     ATENCIÓN DE PACIENTES EN CLÍNICA   

# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Resolver el siguiente problema, diseñando las funciones a utilizar: 
# Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción 
# indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 
# 0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita: 
# a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en 
# el orden que llegaron a la clínica. 
# b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por 
# urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado. 

def registrar_paciente():
    pacientes = []
    while True:
        numero_afiliado = int(input("Ingrese el número de afiliado del paciente (-1 para salir): "))
        if numero_afiliado == -1:
            break
        tipo_atencion = int(input("¿Viene por urgencia (0) o con turno (1)? "))
        pacientes.append((numero_afiliado, tipo_atencion))
    return pacientes

def listar_pacientes(pacientes):
    pacientes_urgencia = [paciente for paciente in pacientes if paciente[1] == 0]
    pacientes_turno = [paciente for paciente in pacientes if paciente[1] == 1]
    
    print("Pacientes atendidos por urgencia:")
    for paciente in pacientes_urgencia:
        print("Número de afiliado:", paciente[0])
    
    print("\nPacientes atendidos por turno:")
    for paciente in pacientes_turno:
        print("Número de afiliado:", paciente[0])

def buscar_paciente(pacientes):
    while True:
        numero_afiliado = int(input("Ingrese el número de afiliado a buscar (-1 para salir): "))
        if numero_afiliado == -1:
            break
        veces_turno = sum(1 for paciente in pacientes if paciente[0] == numero_afiliado and paciente[1] == 1)
        veces_urgencia = sum(1 for paciente in pacientes if paciente[0] == numero_afiliado and paciente[1] == 0)
        print("El paciente con número de afiliado", numero_afiliado, "fue atendido", veces_turno, "veces por turno y", veces_urgencia, "veces por urgencia.")


pacientes = registrar_paciente()


listar_pacientes(pacientes)


buscar_paciente(pacientes)

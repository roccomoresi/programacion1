# Rocco Moresi
# Promedio de curso
# 18/03/2024

def realizarSuma(lista):
    nota = int(input("Ingresa la nota del alumno: "))
    while nota != -1:
        nota = int(input("Ingresa la nota del alumno: "))
        lista.append(nota)
        suma = 0
        suma = suma + nota
        listaFinal = lista.pop()
    return suma
        
    

def realizarPromedio(lista, suma):
    promedio = suma / len(lista)   
    return promedio
    
notas = []
    
result = realizarSuma(notas)
promedio = realizarPromedio(notas, result)

print("El promedio de todo el curso seria:\t", promedio)
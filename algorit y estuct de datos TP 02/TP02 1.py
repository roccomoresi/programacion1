# Título: TP02-01 -     MATERIAS CURSANDO 
# Fecha: 4-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:Escribí un programa donde se declare dentro del mismo código una lista con todas las materias que estás cursado en la
# facultad (no es necesario cargarla con input). A continuación, programar un bucle para listar por pantalla dichas
# materias, cada materia en una línea.

import random

materias = ['Algoritmos y estructura de datos', 'Sistemas Operativos', 'Sistemas de informacion 2', 'Testing de aplicaciones']

for i in range(4):
    print(materias[i],"\n")

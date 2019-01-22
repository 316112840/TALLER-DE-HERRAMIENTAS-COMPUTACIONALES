#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 12, lista de listas'''

#Listas A = [calificaciones[semestres[materias[[parciales,tareas,asistencias]]]]
Alumnos = []
Alumnos.append([[[[5,8,9],[8,7,9],[6,7,10]], [[8,9,7],[6,7,8],[6,7,8]]]  ,  [[[5,8,9],[8,7,9],[6,7,10]] , [[6,7,8],[9,8,7]] ]]) #Semestre 1
Alumnos.append([[[[5,7,9],[6,8,9],[8,10,10]], [[9,9,9],[9,8,8],[9,7,7]]]  ,  [[[6,8,7],[7,7,9],[10,7,10]] , [[10,7,9],[10,9,7]] ]]) #Semestre 2

for calificaciones in Alumnos:
    for semestres in calificaciones :
        for materias in semestres:
            for parciales in materias:
               print parciales,
    print
               
S= "====================================================================="
print S



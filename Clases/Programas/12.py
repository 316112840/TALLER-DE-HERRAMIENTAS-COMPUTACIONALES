#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 12'''

alumnos = []
alumnos.append([9, 8, 10, 9])
alumnos.append([9])
alumnos.append([6, 9, 10, 8, 9, 10, 10, 9])
S = "========================================================"
print alumnos

   
print S

for i in range(len(alumnos)):
    for j in range(len(alumnos[i])):
        calificacion = alumnos[i][j] #De la i-ésima lista estoy escogiendo el j-ésimo elemento.
        print '%4d' % calificacion, #La coma sirve para definir salto de línea
    print 
    
print S

for lista in alumnos:
    for calificacion in lista:
        print '%4d' % calificacion,
    print

print S


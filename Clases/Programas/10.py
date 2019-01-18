#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Esto es lo hicimos la clase 10 del curso, convertir de °C a °F y viceversa, de tres maneras diferentes '''

#Con while:
S=  '==============================================================='
C = -20
iC = 5
print '    C    F'
while C <= 40:
    F = (9.0/5)*C + 32
    print '%5d %5.1f' % (C,F)
    C = C +iC #Esto es una asignación, lo que está a la derecha se evalúa y se guarda en la variable "C"
    #Esto se puede escribir también como "C += iC"

print S

#Con for:
gradosC = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print '    C    F'
for grado in gradosC:
    F = (9.0/5)*grado + 32
    print '%5d %5.2f' % (grado, F) #el 5 es para indicar que habrá 5 espacios a la izquierda del resultado, y donde hay .2 es para que el resultado tenga dos decimales
    
print S

#Con while y la lista:
indice = 0
print '     C     F'
while indice < len(gradosC):
    C = gradosC[indice]
    F = (9.0/5)*C + 32
    print '%5d %5.1f' % (C,F)
    indice += 1

print S

gradosC = []
for C in range(-20,45,5): #Para cada uno de la lista que va del -20 hasta el 45 y va de 5 en 5 (No incluye al 45)
    gradosC.append(C)
print gradosC
#range es una función y append, un método.
#Esta es una forma más difícil de escribir: gradosC = range(-20,45,5)

print S

gradosC = []
for i in range(0,21):
    C = -20 + i*2.5
    gradosC.append(C)
print gradosC

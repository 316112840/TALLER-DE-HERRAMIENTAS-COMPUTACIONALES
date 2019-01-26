#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema5. Soluciones'''

from Problema5 import f

print """La lista que contiene el resultado de evaluar la función dada,
desde x = -2 hasta x = 2 y desde y = 0 hasta y = 3, ambas con un
incremento de 0.5 es: """, f(-2,2,0.5,0,3,0.5)

x1 = input("Ingrese el límite izquierdo en X: ")
x2 = input("Ingrese el límite derecho en X: ")
a = input("Ingrese el incremento deseado de los valores de X: ")
y1 = input("Ingrese el límite izquierdo en Y: ")
y2 = input("Ingrese el límite derecho en Y: ")
b = input("Ingrese el incremento deseado en los valores de Y: ")
print f(x1,x2,a,y1,y2,b)

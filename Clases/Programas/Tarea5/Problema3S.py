#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3 con listas. Soluciones '''

from Problema3 import Cel


n = input("¿CUÁNTOS GRADOS CELSIUS DESEA INGRESAR?")
a=0
C = []
while a < n:
    a += 1
    c = input("Ingrese el grado Celsius: ")
    C.append(c)

print "Los grados Fahrenheit correspondientes a los grados Celsius que escribió se encuentran en esta lista: ", Cel(C)

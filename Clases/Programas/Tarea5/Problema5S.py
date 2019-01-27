#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5. Soluciones'''
from Problema5 import suma

x = input("¿Cuántos números quiere introducir? ")
a = 0
while a < x:
    a += 1
    y = input("Introduzca el número: ")
    print "La suma de los primeros %d números es %d" %(y,suma(y))

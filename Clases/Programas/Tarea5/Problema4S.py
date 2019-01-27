#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 4: Sucesión de Fibonacci. Soluciones'''

from Problema4 import *

y = input("¿Cuántos números desea ingresar? ")
a = 0
while a < y:
    a += 1
    x= input("Ingrese el número: ")
    print Fib3(x)

#Este método se tarda en dar el resultado pero sí lo hace

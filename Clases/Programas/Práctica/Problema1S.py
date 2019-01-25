#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema1. Soluciones'''

from Problema1 import Grados

y = 1
x = input("¿Cuántos grados quiere introducir?")
while y <= x:
    y = y + 1
    g = input("Ingrese el grado Faherenheit: ")
    Grados(g)
    

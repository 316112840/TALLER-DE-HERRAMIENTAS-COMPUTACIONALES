#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema1. Soluciones'''

from Problema1 import Grados

x = ("¿Cuántos grados quiere introducir?")
y = 0
while y <= x:
    x = ("¿Cuántos grados quiere introducir?")
    y = y + 1
    gradoF = input("Ingrese el grado Faherenheit: ")
    print Grados(gradoF)

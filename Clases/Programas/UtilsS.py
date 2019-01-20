#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Funión range pero con un incremento flotante, soluciones'''


import utils
print utils.rangef(1,6,0.25)

x = input("Ingrese el número inicial: ")
y = input("Ingrese el número final: ")
z = input("Ingrese el incremento: ")
print"La lista que empieza en %d termina en %d con un incremento de %f es:"%(x, y,z), utils.rangef(x,y,z)

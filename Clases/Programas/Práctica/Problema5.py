#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema5'''

from Problema4 import Range

def f(x1,x2,a,y1,y2,b):
    F = []
    F1 = []
    F2= []
    h = 0
    for i in Range(x1,x2,a):
        F.append(i)
    for j in Range(y1,y2,b):
        F1.append(j)
    g = len(F)*len(F1)
    while h < g:
        h += 1
        f = (F[h]**2)/25.0 - (F[h]**2)/49.0
        F2.append(f)
    print F2
    print F, F1, g, F2
    

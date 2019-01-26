#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema5'''

from Problema4 import Range

def f(x1,x2,a,y1,y2,b):
    F = []
    for i in Range(x1,x2,a):
        for j in Range(y1,y2,b):
            F.append([i,j])
    return F
#h = [(i**2)/25.0 - (j**2)/49.0 in F]
   
   

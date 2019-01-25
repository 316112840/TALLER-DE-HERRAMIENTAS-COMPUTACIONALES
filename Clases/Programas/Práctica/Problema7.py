#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema7'''

from math import sin
from math import pi 
def H_eps(x,e=0.01):
    if x < -e:
        return 0
    elif -e <= x <= e :
        H = 1.0/2 + x/(2*e)* sin((pi * x)/2.0)
        return H
    else:
        return 1

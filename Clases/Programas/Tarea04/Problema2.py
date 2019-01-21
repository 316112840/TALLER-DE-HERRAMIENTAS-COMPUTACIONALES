#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 2'''

import math
def tiempo(v0,h):
    a = 9.81
    v0 = v0
    h = h
    t1 = (v0 + math.sqrt(v0**2 - 2*a*h))/a
    t2 = (v0 - math.sqrt(v0**2 - 2*a*h))/a
    print "Los tiempos donde se alcanza la altura %f m son %f y %f"%(h, t1, t2)



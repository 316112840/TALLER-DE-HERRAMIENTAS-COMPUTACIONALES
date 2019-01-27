#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 6'''


def promedio(x):
    a = 0
    b = 0
    while a < len(x)-1:
        a += 1
        b = b + x[a]
    return (b + x[0])/float(len(x))
    

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 usando listas'''

def MCD(x,y):
    L = []
    x = x
    y = y
    r = x%y
    while r != 0:
        x = y
        y = r
        r = x%y
        L.append(y)
    return L
    print"El máximo común divisor es: %f" %(L.pop(len(L) - 1))
    

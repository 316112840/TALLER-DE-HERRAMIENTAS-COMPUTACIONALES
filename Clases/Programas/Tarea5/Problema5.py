#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5'''

def suma(x):
    a = 0
    S =[]
    b = 0
    while a < x:
        a += 1
        S.append(a)
    for num in S:
        b = b + num
    return b 

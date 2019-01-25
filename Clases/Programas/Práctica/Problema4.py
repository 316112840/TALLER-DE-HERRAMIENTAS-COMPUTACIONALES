#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema4'''

def Range(a, b, c):
    L = []
    i = 0
    a = a
    while a<b:
        i = i + 1
        a = a + c
        L.append(a)
    return L 

def malla(a,b,c, d, e ,f):
    M = []
    for i in Range(a, b, c):
        M.append([i])
        for j in Range(d,e, f):
            M.append([i,j])
    return M

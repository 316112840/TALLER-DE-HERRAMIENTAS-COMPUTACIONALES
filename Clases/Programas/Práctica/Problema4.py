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

def malla():
    M = []
    for i in Range(-5, 5, 0.5):
        M.append([i])
        for j in Range(-7,7, 0.5):
            M.append([i,j])
    return M

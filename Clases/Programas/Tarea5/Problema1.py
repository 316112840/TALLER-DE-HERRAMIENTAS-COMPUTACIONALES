#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 usando listas'''



def MCD(a,b):
    A = []
    r = a%b
    if a<b:  
        tmp = b
        b = a
        a = tmp
    while r != 0:
        a = b
        b = r
        r = a%b
    A.append(b)
    for i in A:
        return i

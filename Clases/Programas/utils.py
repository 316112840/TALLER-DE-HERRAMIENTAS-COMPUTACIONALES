#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Funión range pero con un incremento flotante'''



def rangef(a, b, c):
    L = []
    while a <= b - c:
        a = a + c
        L.append(a)
    print L


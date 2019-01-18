#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1'''



def mcd(a,b):
    a = a
    b = b
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
    print"El máximo común divisor es: %f" %(b)


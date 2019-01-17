#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1'''



def mcd(a,b):
    if a<b:  #Este bloque if se coloca para intercambiar las variables cuando "a" es menor que "b"
        tmp = b
        b= a
        a = tmp
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b



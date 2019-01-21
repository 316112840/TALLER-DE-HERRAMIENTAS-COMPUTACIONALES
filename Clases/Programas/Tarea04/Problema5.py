#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5'''


def SumaN(n):
    i = 0
    A0 = 0
    A1 = 1
    while n > i:
        i = i + 1
        A0 = A0 + A1
        A0 = A0 + n
    print "La suma de los primeros %d naturales positivos es: %d" % (n, A0/2)


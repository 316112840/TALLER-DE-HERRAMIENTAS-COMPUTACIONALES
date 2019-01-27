#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 8 del libro Python facil, página 58'''

def g(l):
    a = 0
    for i in l:
        for j in l:
            if abs(i-j) > a:
                a = abs(i-j)
    return a



""" Al dar la lista "l" que contenga dos o más elementos, si el valor absoluto
de la resta de dos elementos de la lista es mayor a 0 (por definición de valor
abosoluto esto se cumplirá), te regresará el valor absoluto del resultado de la
resta. Si se incluyen más de dos elementos, te mostrara el valor absoluto mayor.
"""

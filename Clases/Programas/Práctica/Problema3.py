#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema3'''

def SumaCubos(n):
    cubo =  n **3
    if n>1:
        return cubo + SumaCubos(n-1)
    else:
        return cubo

def comparar(n):
    return (n*(n + 1)/2)**2

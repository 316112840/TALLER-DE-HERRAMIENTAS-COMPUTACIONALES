#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema2'''


def SumaCuadrados(n):
    cuadrado = n **2
    if n > 1:
        return cuadrado + SumaCuadrados(n-1)
    else:
        return cuadrado


     
def comparar(n):
    return (n*(n + 1)*(2*n + 1))/6
    

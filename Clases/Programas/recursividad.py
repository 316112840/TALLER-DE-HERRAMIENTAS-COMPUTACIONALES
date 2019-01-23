#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Esto es lo que se vió el miércoles 23 de enero. Recursividad'''

def fib(n):
    """ Calculo el nesimo termino de la suc
de fib con n natural
"""
    if  n > 2:
        return fib(n-1) + fib(n-2)
    else:
        return 1

    
def Suma(n):
    """ Calculo de la suma del 1 al nésimo término
"""
    if n > 1:
        return n + Suma(n-1)
    else :
        return 1

def printR(L):
    if len(L)>1:
        print L[0],
        printR(L[1:])
    else:
        print L[0]
    
L = [1,2,4,5,9]
printR(L) 

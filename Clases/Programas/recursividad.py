#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Esto es lo que se vió el miércoles 23 de enero. Recursividad'''
#http://www.pythontutor.com/visualize.html  en esta página podemos ver el procedimiento de cómo se está ejecutando un programa.

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

def printR(L): #Cuando la longitud de L es mayor a 1, mostrará el primero y procesará el resto. Y así sucesivamente hasta que solo haya uno y lo va a mostrar.
    if len(L)>1:
        print L[0], #La coma (,) omite el salto de línea
        printR(L[1:])
    else:
        print L[0]
    
def printr(L):
    if L: #En este caso se usa lo de "Si una lista es vacía se toma como falso"
        print L[0],
        printr(L[1:])

L = [1,2,4,5,9]
printR(L)
printr(L)
#printR y printr son dos formas de hacer lo mismo.

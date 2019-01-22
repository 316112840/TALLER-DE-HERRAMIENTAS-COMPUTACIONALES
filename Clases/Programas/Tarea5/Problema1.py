#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 usando listas'''

def MCD(x,y):
    L = [] #Esta es una lista vacía
    r = x%y
    while r != 0:
        x = y
        y = r
        r = x%y
        L.append(y) #A la lista le iré incluyendo los valores que "y"
    print ("Máximo común divisor: " ), L[len(L)-1] #Imprimirá el último valor de la lista
    

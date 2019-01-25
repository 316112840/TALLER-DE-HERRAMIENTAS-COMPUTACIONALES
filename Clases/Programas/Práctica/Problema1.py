#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema1'''

def Grados(F):
    C = (F - 30)/2
    C1 = 5*(F -32)/9
    if  C < C1:
        diferencia = C1 - C
    else :
        diferencia = C -C1
    y = [F]
    y.append(C1)
    y.append(C)
    y.append(diferencia)
    for resultado in y:
        print resultado,
    print 
    

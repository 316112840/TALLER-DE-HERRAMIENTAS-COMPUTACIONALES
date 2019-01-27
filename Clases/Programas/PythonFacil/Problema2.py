#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 2 del libro Python facil, página 58'''

def suma(y):
    if len(y)> 1:
        return y[0] + suma(y[1:])
    else:
        return y[0]


def suMatriz(M):
    b = -1 #Para que al sumar le 1 sea 0 y empiece con M[0]
    S = []
    while b < len(M)-1 :
        b += 1
        y = sum(M[b])
        S.append(y)
    return S


def suMatriz2(M):
    A = []
    for i in M:
        A.append(sum(M[0][0]))
        return A

        
    

M = [[7,2,3],[2,11,7],[12,5,8], [1,6,9]]
print suMatriz2(M)
    

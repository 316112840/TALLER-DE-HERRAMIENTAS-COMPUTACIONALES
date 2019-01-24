#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5, laberinto'''

L = [[True, True, True, True], [False, False, False, False], [True, True, True, True]]
M = [[True, True, True, True],[False, False, False, True], [True, True, False, True]]
#L es el laberinto, e es la entrada e=[x, y+1]. Y hay que buscar S que es la salida.
def resolver(L, e):
    n = len(L[0]) -1
    m = len(L)-1
    x = e[0]
    y = e[1]
    if y == n or x==m:
        return e[0]+1, e[1]+1 #de esta forma el resultado se mostrará como tupla
    elif y != n:
        if L[x][y+1] == False:
            e = [x, y+1]
            return resolver(L, e) # la entrada ahora es e = [x, y+1]
        elif x != m:
            if L[x + 1][y] == False:
                e = [x+1, y]
            return resolver(L, e) 

e = [1,0]
r = resolver(L, e)
print resolver(L,e)
print resolver(M,e)


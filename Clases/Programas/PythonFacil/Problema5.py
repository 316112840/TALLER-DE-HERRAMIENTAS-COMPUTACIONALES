#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5, laberinto'''

L = [[True, True, False, True, True], [False, False, False, True, True], [True, True, True, True, True]]

#L es el laberinto, E es la entrada. Y hay que buscar S que es la salida.

def laberinto(L, e):
    """ Este programa te permitirá
encontar la salida del laberinto
que se dé"""
    n = len(L[0])  - 1
    m = len(L) - 1
    x = e[0]
    y = e[1]
    if y == n or x == m:
        return e[0]+1, e[1]+1 
    elif y<n and x<m:
        if L[x][y+1] == False:
            e = [x, y+1]
            return laberinto(L, e)
        elif L[x + 1][y] == False:
            e = [x+1, y]
            return laberinto(L, e)
        #if L[x][y -1] == False:  ESTO ESTÁ MAL
        #    e = [x, y - 1 ]
         #   return laberinto(L,e)
       # elif L[x-1][y] == False : ESTO ESTÁ MAL 
        #    e = [x-1,y]
         #   return laberinto(L,e)
        else:
            return "Ya no se puede seguir avanzando"
    
print laberinto(L,[0,1])

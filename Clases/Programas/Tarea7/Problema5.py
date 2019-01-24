#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 5, laberinto'''

L = [[True, True, True], [False, False, False], [True, True, True]]

#L es el laberinto, E es la entrada. Y hay que buscar S que es la salida.
def laberinto(L, E):
    """ Este programa te permitirá
encontar la salida del laberinto
que se dé y la entrada"""
    n = len(L[0])
    m = len(L)
    
    

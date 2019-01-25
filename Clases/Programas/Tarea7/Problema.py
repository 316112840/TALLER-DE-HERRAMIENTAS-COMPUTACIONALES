#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 del libro Python facil, página 58'''

def Listas(L1, L2):
    if L1 == L2: 
        return ("Ambas listas son iguales.")
    else:
        return ("Ambas listas no son iguales")

x = input("INGRESE SU LISTA DE LA FORMA [a,b,c,]: ")
y = input("INGRESE LA SEGUNDA LISTA DE LA FORMA [a,b,c]: ")
print Listas(x,y)

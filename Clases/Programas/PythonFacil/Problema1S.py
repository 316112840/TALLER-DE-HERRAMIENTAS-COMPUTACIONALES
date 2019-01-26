#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 del libro Python facil, página 58. Solución'''

from Problema import Listas

x = input("INGRESE SU LISTA DE LA FORMA [a,b,c,]: ")
y = input("INGRESE LA SEGUNDA LISTA DE LA FORMA [a,b,c]: ")
print Listas(x,y)



L1 = [1,2,3,4,5,6,7,10]
L2 = [1,2,3,4,7,9,12,34]
print "LISTA1 = ",L1,"LISTA2 = " ,L2, Listas(L1,L2)

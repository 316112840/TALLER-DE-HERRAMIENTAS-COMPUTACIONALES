#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 11: Grados C y grados F. Soluciones'''

from grados import *
L1 = listaC(-15,32,10)
L2 = listaF(L1)
mostrarListas(L1,L2)
mostrarListas1(L1,L2)

a = input("¿Cuál es el extremo izquierdo del intervalo? ")
b = input("¿Cuál es el extremo derecho del intervalor? ")
n = input("Cuántos subintervalos? ")
L1 = listaC(a,b,n)
L2 = listaF(L1)
mostrarListas(L1,L2)

        

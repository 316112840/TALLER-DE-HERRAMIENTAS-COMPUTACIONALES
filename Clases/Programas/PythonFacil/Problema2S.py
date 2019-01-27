#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 2 del libro Python facil, página 58. Soluciones'''

from Problema2 import suMatriz

a = input("¿Cuántas listas tendrá su matriz? ")
b = 0
M = []
while b < a:
    b += 1
    x = input("""Ingrese el contenido de la primera lista, de la forma [a,b,c,d...].
La longitud de las listas deben ser la misma. """)
    M.append(x)
print suMatriz(M) #Esta es la suma de las filas, falta la suma de las columnas




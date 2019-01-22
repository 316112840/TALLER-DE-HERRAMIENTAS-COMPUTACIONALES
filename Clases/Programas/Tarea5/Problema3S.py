#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3 con listas. Soluciones '''

from Problema3 import Cel

C = []
n = input("¿CUÁNTOS GRADOS CELSIUS DESEA INGRESAR?")
c = input("Ingrese el grado Celsius: ")
C.append(c)

while c < n:
    c = input("Ingrese el grado Celsius: ")
    C.append(c)
print (C)
for i in C:
    print (Cel(i))

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3, SOLUCIONES'''

import Problema3
Problema3.CeFa(78)
Problema3.FaCe(172.4)

z = input("¿Quiere transformar de °C a °F?(S/N) ")
if z == "S" or z== "s":
    x = input("Escribe los °C que quieras transformar a °F:")
    print Problema3.CeFa(x)
if z=="N" or z=="n":
    y = input("Escribe los °F que quieras transformar a °C:")
    print Problema3.FaCe(y)

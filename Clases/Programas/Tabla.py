#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 11: Grados C y grados F. Tabla'''

from grados import *

gradosC = [-5 + i*0.5 for i in range(12)]
gradosF = [9.0/5 *c + 32 for c in gradosC]

i = 0
while i<12:
    i= i +1
    print gradosC[i], gradosF[i]


tabla = zip (gradosC, gradosF)
for i in tabla:
    print  i

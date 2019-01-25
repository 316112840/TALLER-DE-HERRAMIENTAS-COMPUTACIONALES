#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Examen práctico. Problema7. Soluciones'''

from Problema7 import H_eps


print"Cuando x < -e :", H_eps(-5) # x < -e
print "Cuando x = -e :", H_eps(-0.001) # x == -e
print "Cuando x = 0 :",H_eps(0) # x == 0
print "Cuando x = e :",H_eps(0.001) # x == e
print "Cuando x > -e :",H_eps(1) # x > -e

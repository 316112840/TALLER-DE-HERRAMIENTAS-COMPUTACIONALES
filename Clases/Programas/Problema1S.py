#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1 Solcuciones'''

import Problema1
a = input("Ingrese el entero mayor: ")
b = input("Ingrese el entero menor: ")
print "El M.C.D de %d y %d es %d"%(a,b,Problema1.mcd(a,b))


#Esto también podía escribirse así:
#from Problema1 import mcd
#a = input("Ingrese el entero mayor: ")
#b = input("Ingrese el entero menor: ")
#print "El M.C.D de %d y %d es %d"%(a,b,mcd(a,b))

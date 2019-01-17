#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3'''


#Para transformar de °F a °C:
def FaCe(a):
    f = a
    c  = (a - 32)/1.8
    return c

#Para transformar de °C a °F:
def CeFa(y):
    c = y
    a = y*1.8 +32
    return a


print CeFa(78)
print FaCe(172.4)


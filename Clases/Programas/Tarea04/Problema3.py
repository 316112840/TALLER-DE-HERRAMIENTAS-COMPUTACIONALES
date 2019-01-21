#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3'''


#Para transformar de °F a °C:
def FaCe(f):
    c  = (f - 32)/1.8
    return c

#Para transformar de °C a °F:
def CeFa(c):
    f = c*9/5 +32
    return f


print CeFa(78)
print FaCe(172.4)


#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 7 del libro Python facil, página 58'''

def f(l):
    a = 0
    b = 0
    for i in l:
        if i > 0:
            a += i
        else:
            a -= i
    return a + b

"""Al ingresar una lista "l", si "l" tiene más de 0 números dentro de ella los sumará.
si esto no se cumple, es decir, si tiene 0 elementos le restará "b" y como b es igual
a 0 te mostrará el resultado de restar 0 menos 0, es decir, 0."""

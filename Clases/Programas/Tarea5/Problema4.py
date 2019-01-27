#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 4: Sucesión de Fibonacci'''

def Fib(x):
    if x > 2:
        return Fib(x-1) + Fib(x-2)
    else:
        return 1


def Fib2(x):
    F = []
    b = 0
    while b < x:
        b += 1
        F.append(Fib(b))
        a = 0
    return F

def Fib3(x):
    F = []
    b = 0
    a = 0
    while b < x:
        b += 1
        a = a + Fib(b)
    F.append(a)
    for i in F:
        return"El numero coorespondiente de la sucesion al numero que escribio es: %d" % i
           


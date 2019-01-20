#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 4: Sucesión de Fibonacci'''

#0 1 1 2 3 5 8 13 21 34 55 89 144

def Fibonacci(n):
    i = 0
    A0 = 0
    A1 = 1
    A2 = 1
    A3 = 1
    if n%2 == 0:
        n = n//2
        while n  > i :
            i = i + 1
            A0 = A0 + A1
            A1 = A1 + A0
        print "El número de la sucesión que corresponde al dígito %d es: %d" %(n*2,A1)
    else:
        n = n//2
        while n > i :
            i = i + 1
            A2 = A2 + A3
            A3 = A3 + A2
        print "El número de la sucesión que corresponde al dígito %d es: %d" %(n*2 + 1, A3)


    

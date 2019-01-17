#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 1'''


x = input("Escriba el primer número:")
y = input("Escriba el segundo número:")

def mcd(k,p):
    a = 1
    while k%a == 0 and p%a==0 and a==a:
        b = k/a
        c = p/a
        a = a + 1
    return a 

print"El máximo común divisor es: %d" %(mcd(x,y))


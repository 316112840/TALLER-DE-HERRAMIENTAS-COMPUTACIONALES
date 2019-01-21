#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 11 del curso '''

n= input(¿Cuántos valores?)

#Esta es una forma de hacerlo:
for i in range(n):
    valor = input("Escribe el valor: ")
    L.append(valor)

#Esta es otra:
M= range(n)
for i in M:
    valor = input("Dame el valor: ")
    M[1](valor)

#Esta es otra forma:
N = range(n)
j = 0
while j < n:
    valor = input("Dame el número: ")
    N[1](valor)
    

L = range(n)
print "La lista tiene %d valores" %(len(L))
print L

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3 del libro Python facil, página 58. Soluciones'''
from Problema3 import primo

x = input("¿De cuántos números quiere saber si son primos?")
a = 0
while a < x:
    a += 1
    y = input("Ingrese el primer número: ")
    print primo(y)

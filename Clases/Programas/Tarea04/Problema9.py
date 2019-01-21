#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 9'''

 #Este programa sumará todos los números que de el usuario hasta que escriba una ""


def Suma(y):
    x=0
    while y >= 0:
        y = input("Ingrese el primer número, si quiere detener la suma escriba un número menor a 0: ")
        x = x + y
        if y < 0:
            print("La suma de los números anteriores es: "), x
            break
        print x

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 2.Listas'''
import math

def Tiempo(v0,h):
    a = 9.81
    V =[]
    V.append(v0)
    H = []
    H.append(h)
    for i in V:
        for j in H:
            if (v0**2 - 2*a*h)>0:
                t1 = (v0 + math.sqrt(v0**2 - 2*a*h))/a
                t2 = (v0 - math.sqrt(v0**2 - 2*a*h))/a
                return "Los tiempos donde se alcanza la altura %f m son %f y %f"%(h, t1, t2)
            else:
                return"Los tiempos donde se alcanza la altura %d m con velocidad inicial igual a %d no están dentro de los numeros Reales" %(h,v0)
        



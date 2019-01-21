#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 11: Grados C y grados F '''

def listaC(cmin,cmax,n):
    gradosC = []
    dC = (cmax - cmin)/float(n-1) #Se convierte en flotante por si al final queda entero/entero y que el resultado pueda ser flotante
    # for(i=0; i<n; i++)  Así se escribiría en otros lenguajes.
    for i in range(n): #range(n) crea una lista que va del 1 al n
        C = cmin + i*dC #Esta es una asignación
        gradosC.append(C) #Este es un llamado a append para el objeto gradosC
    return gradosC

def listaF(gradosC):
    gradosF = []
    for C in gradosC: #Por cada uno de los grados en la lista de gradosC voy a hacer un proceso y el resultado lo incluiré a la lista gradosF.
        F = (9.0/5)*C + 32
        gradosF.append(F)
    return gradosF

def mostrarListas(gradosC, gradosF):
    for i in range(len(gradosC)): #Usamos la i regularmente para contar pero podríamos poner cualquier otra variable.
        C = gradosC[i]
        F = gradosF[i]
        print "%5.1f %5.1f" % (C, F)

def mostrarListas1(gradosC, gradosF):
    for C,F in zip(gradosC, gradosF):
        print "%5d %5.1f" % (C,F)

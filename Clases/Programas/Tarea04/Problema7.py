#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 7'''
import Problema6
def mayor(a,b,c,d,e,f,g,h,i,j):
    a,b,c,d,e,f,g,h,i,j=a,b,c,d,e,f,g,h,i,j
    if a<b:
        tmp=a
        a=b
        b=tmp
    if a<c:
        tmp=a
        a=c
        c=tmp
    if a<d:
        tmp=a
        a=d
        d=tmp
    if a<e:
        tmp=a
        a=e
        e=tmp
    if a<f:
        tmp=a
        a=f
        f=tmp
    if a<g:
        tmp=a
        a=g
        g=tmp
    if a<h:
        tmp=a
        a=h
        h=tmp
    if a<i:
        tmp=a
        a=i
        i=tmp
    if a<j:
        tmp=a
        a=j
        j=tmp
    print "El mayor es: %d"%a
    
def menor(a,b,c,d,e,f,g,h,i,j):
    a,b,c,d,e,f,g,h,i,j=a,b,c,d,e,f,g,h,i,j
    if a>b:
        tmp=a
        a=b
        b=tmp
    if a>c:
        tmp=a
        a=c
        c=tmp
    if a>d:
        tmp=a
        a=d
        d=tmp
    if a>e:
        tmp=a
        a=e
        e=tmp
    if a>f:
        tmp=a
        a=f
        f=tmp
    if a>g:
        tmp=a
        a=g
        g=tmp
    if a>h:
        tmp=a
        a=h
        h=tmp
    if a>i:
        tmp=a
        a=i
        i=tmp
    if a>j:
        tmp=a
        a=j
        j=tmp
    print"El menor es %f"%a
    
def mmp(a,b,c,d,e,f,g,h,i,j):
    a,b,c,d,e,f,g,h,i,j=a,b,c,d,e,f,g,h,i,j
    print menor(a,b,c,d,e,f,g,h,i,j)
    print mayor(a,b,c,d,e,f,g,h,i,j)
    print Problema6.promedio(a,b,c,d,e,f,g,h,i,j)

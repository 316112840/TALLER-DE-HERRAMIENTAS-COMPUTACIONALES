#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Esto es lo que se hizo la clase 14'''

adn = 'ATGCGACCTAT'
base = 'C'

def contar_v1(adn,base): #Versión 1
    adn=list(adn)
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i
v1 = contar_v1(adn, base)
print '%s aparece %d veces en %s' % (base, v1, adn)


def contar_v2(adn, base): #Versión 2
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i 
v2 = contar_v2(adn, base)
print '{base} aparece {v2} veces en {adn}' .format(base=base, v2=v2, adn=adn)


def contar_v3(adn, base): #Versión 3
    i = 0
    for j in range(len(adn)):
        if adn[j] == base:
            i +=1
    return i
print contar_v3(adn,base)


def contar_v4(adn, base): #Versión 4
    i = 0
    j = 0
    while j < len(adn):
        if adn[j] == base:
            i += 1
        j += 1
    return i
v3= contar_v4(adn, base)
print '%s aparece %d veces en %s' % (base, v3, adn)






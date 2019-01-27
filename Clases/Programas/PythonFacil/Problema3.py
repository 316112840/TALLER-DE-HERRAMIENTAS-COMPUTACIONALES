#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Problema 3 del libro Python facil, página 58'''

def primo(x):
    if x%2 ==0 and x != 2:
       return "No es numero primo"
    elif x%3 == 0 and x != 3:
        return "No es numero primo"
    elif x%4 == 0 and x != 4:
        return "No es numero primo"
    elif x%5 == 0 and x != 5:
        return "No es numero primo"
    elif x%6 == 0 and x != 6:
        return "No es numero primo"
    elif x%7 == 0 and x != 7:
        return "No es numero primo"
    elif x%8 == 0 and x != 8:
        return "No es numero primo"
    elif x%9 == 0 and x != 9:
        return "No es numero primo"
    else:
        return "Es numero primo"
    

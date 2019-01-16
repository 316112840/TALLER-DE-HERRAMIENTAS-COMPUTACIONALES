#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
Esto es lo que vimos el miércoles '''
#En la línea 4 se escribirá un pequeño cometario sobre lo que se hizo en este archivo.

x = 10.5; y = 1.0/3; z = 15.3
# Esta es otra forma de escribir las variables: x,y,z=10.5,1.0/3,15.3
H = '''
El punto en R3 es:
(x,y,z)=(%.2f,%g,%G)
''' % (x,y,z)
print H

G = '''
El punto en R3 es:
(x,y,z)=({laX:.2f},{laY:g},{laZ:G}
'''.format(laX=x,laY=y,laZ=z)
print G
#Si una variable aparece más de una vez aquí no es necesario escribirlo mas de una vez como en el caso de la H


import math as m
from math import sqrt #Este importa unicamente la función sqrt del módulo math
from math import * #Este importa todas la funciones por lo que no es recomendable porque guarda espacio.
from math import sqrt as s #Con esto renombramos a sqrt como s, de esta manera cada que usemos sqrt no será neceario escribir todo, bastará con escribir s.
x=16
x=input("Cuál es el valor al que le quieres" + "calcular la raíz") #Permite al usuario interactuar con el programa
print "La raiz cuadrada de %.2f es %f"%(x,m.sqrt(x))
print sqrt(16.5)
print s(16.5)

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
''' Marínez García Mariana Yasmin
316112840
Taller de Herramientas Computacionales
clase 11: Grados C y grados F. Tabla'''

gradosC = [-5 + i*0.5 for i in range(12)]
gradosF = [9.0/5 *c + 32 for c in gradosC]
tabl = zip (gradosC, gradosF)
L = []
x = tuple(tabl)
for i in x:
    #print(i)
    y = i
    for j in y:
        #print(j)
        L.append(j)
#print(L)
A = [L[0], L[1]]
print (A)
B = [L[2], L[3]]
print (B)
C = [L[4], L[5]]
print (C)
D = [L[6], L[7]]
print (D)
E = [L[8], L[9]]
print (E)
F = [L[10], L[11]]
print (F)
G = [L[12], L[13]]
print (G)
H = [L[14], L[15]]
print (H)
I = [L[16], L[17]]
print (I)
J = [L[18], L[19]]
print (J)
K = [L[20], L[21]]
print (K)
L = [L[22], L[23]]
print (L)
#A pesar de que sí quedó, esto no es lo que se pedía. Debía de ser en comprensión.


S = "============================================================="
print S
tabla = [[C, F] for C,F in zip(gradosC, gradosF)]
print (tabla)

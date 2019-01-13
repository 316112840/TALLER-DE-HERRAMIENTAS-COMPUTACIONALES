# -*- coding: utf-8 -*-
# Martínez García Mariana Yamsin
# Ejercicio sobre tiro vertical
V1 = 0 #Velocidad final
H = 3.2 #Altura máxima alcanzada
m = 0 #Altura inicial
a = 9.81 #La aceleración es la fuerza de gravedad
#V1=V0**2 - 2*a*(H-h)
import math
V0 = math.sqrt(V1 + 2*a*(H - m))
print (V0)

def velocidad0(V1,H,m):
    V0 = math.sqrt(V1 + 2*a*(H - m))
    return(V0)

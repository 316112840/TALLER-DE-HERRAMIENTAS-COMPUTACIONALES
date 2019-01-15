# -*- coding: utf-8 -*-
#Esta es mi versión de Ulam:
def Ulam0(x):
    i = 0
    while x>1:
        if (x/2)*2 -x==0:
            x = x/2
        else:
            x= 3*x +1
        i = i+1
    print"El ciclo se repitió %d veces"%(i)
    
        
        
Ulam0(7)
Ulam0(26)
Ulam0(52)
Ulam0(1024)
Ulam0(72)
Ulam0(1524927)
Ulam0(2)

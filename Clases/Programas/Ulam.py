# -*- coding: utf-8 -*-
def Ulam(x):
    i = 0
    while x>1:
        if (x/2)*2 -x==0:
            x = x/2
        else:
            x= 3*x +1
        i = i+1
    print"El ciclo se repitió %d veces"%(i)
    return(x)
        
        

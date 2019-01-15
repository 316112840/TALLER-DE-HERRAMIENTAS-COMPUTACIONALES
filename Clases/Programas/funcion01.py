# -*- coding: utf-8 -*-
def vAbsoluto(x):
    if x>=0:
        return(x)
    else:          #Si el bloque (lo que está depués de los dos puntos) "if" es falso se hará lo de este bloque.
        return(-x) 

def raiz(x):
    h=x                #Estos son los valores iniciales
    b=1.0   
    e=0.0001
    while vAbsoluto(b-h)>e: #Ciclo while
        h = (b+h)/2         #Bloque asociado a while
        b = x/h
    return(h)

def raiz1(x):
    h=x                
    b=1.0   
    e=0.0001
    while vAbsoluto(b-h)>e: 
        h = (b+h)/2         
        b = x/h
        print"La cantidad de veces que se repitió el procedimento fue h=%g" es %(g)
    return(h)
    

print raiz(1)
print raiz(4)
print raiz(9)
print raiz(9.1)
print raiz(1000000)
#print(x)  No podemos color esto ya que x no está definida


#Los espacion en python solo son importantes cuando defino bloques.
#Que algo haga eco es que muestre el resultado

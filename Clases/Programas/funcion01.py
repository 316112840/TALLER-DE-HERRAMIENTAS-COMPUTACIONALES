# -*- coding: utf-8 -*-
def vAbsoluto(x):
    if x>=0:
        return(x)
    else: #Si el bloque (lo que está depués de los dos puntos) "if" es falso se hará lo de este bloque.
        return(-x) 

def raiz(x):
        h=x   #Aquí están h, b y e, que son los valores iniciales.
        b=1.0   
        e=0.0001  #Esta es la presición de decimales que quiero.
        while vAbsoluto(b-h)>e: #Ciclo while. Mientras se cumpla esto seguirá produciendose el ciclo.
            h = (b+h)/2         #Bloque asociado a while
            b = x/h
        return(h)

def raiz1(x):
        h=x                
        b=1.0   
        e=0.0001 
        i=0   #Cuenta el número de veces que se ejecutó el ciclo while
        while vAbsoluto(b-h)>e: 
            h = (b+h)/2         
            b = x/h
            i = i+1 #Cada vez que el ciclo se repita irá incrementando en 1.
        print"El ciclo se reitió %d veces"%(i)
        return(h)
    

print raiz1(1)
print raiz1(4)
print raiz1(9)
print raiz1(9.1)
print raiz1(1000000)
#print(x)  No podemos color esto ya que x no está definida


#Los espacion en python solo son importantes cuando defino bloques.
#Que algo haga eco es que muestre el resultado

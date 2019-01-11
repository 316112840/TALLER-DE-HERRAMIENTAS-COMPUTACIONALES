# -*- coding: utf-8 -*-
v0 = 34
a = 9.81
t = 4.3
y = v0*t - 1.0/2*a*t**2
#Una cadena en python es una seria de carácteres delimitados por una comilla al principio y otra al final.
#print 'La posición de la pelota en el t=%g es %.2f' % (t,y) #Este muestra el resultado redondeado a dos decimales.
print 'La posición de la pelota en el t=%E es %.2f\n%f' % (t,y,t)

def posicion(t,v0): #voy a definir una función que depende del t y de la v0
    y = v0*t - 1.0/2*a*t**2
    return(y) #la función de regresa a un valor "y".Esto solo lo calcula, si queremos ver el resultado debemos crear otra función para imprimir lo.













# print 'La posición de la pelota en el t=%g es %.4f' % (t,y) #Este muestra el resultado con 4 decimales.
#El primer "%" corresponde al "t" y el segundo, al "y"
# %g es para mostar variables del tipo flotante
# %f mostrará el valor de una constante del tipo flotante
# %s lo va a sustituir por una variable que contenga cadena.
# %d es para dígitos enteros
# %c es para formato científico

# print 'La posición de la pelota en el t=%E es %.2f' %( t,y)
# print 'La posición de la pelota en el t=%E es %.2f\n%f' % (t,y,t) 
#print 'La posición de la pelota en el t=%g es %.2f' % (t,y) #Este muestra el resultado redondeado a dos decimales.

#si yo tengo una variable y quiero mostrar su contenido con "print" tengo que usar la secuencia: %s

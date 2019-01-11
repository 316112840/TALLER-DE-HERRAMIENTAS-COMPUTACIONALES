# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field. Te muestra el resultado sin decimales, NO redondea.

print '"%5d"' % i      # field of width 5 characters. Este te muestra el resultado sin decimales del tamaño de 5 caractéres.
print '"%05d"' % i     # pad with zeros. Es como el anterior solo que llena con "0" los espacios necesarios para que tenga el tamaño de 5 caractéres.

print '"%g"' % r       # r is big number so this is scientific notation. Para cuando r es muy grande y se necesita usar una notación científica.
print '"%G"' % r       # E in the exponent
print '"%e"' % r       # compact scientific notation
print '"%E"' % r       # compact scientific notation
print '"%20.2E"' % r   # 2 decimals, field of width 20
print '"%30g"' % r     # field of width 30 (right-adjusted)
print '"%-30g"' % r    # left-adjust number. Muestra el número a la izquierda, y deja los espacios hasta llenar el número de carácteres pedidos.
print '"%-30.4g"' % r  # 3 decimals. Te lo muestra con tres decimales.

print '%s' % i   # can convert i to string automatically
print '%s' % r

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)




#https://docs.python.org/2/library/math.html  En esta página hay información sobre cómo aplicar funciones matemáticas en python 


from Problema4 import Range

M =[]
a = 0
if -5 <= x <= 5:
    a = a +1
    for i in Range(-5,5,0.5):
        M[a][0]== i
    return M
elif -7 <= x <= 7:
    a = a +1 
    for j in Range(-7, 7, 0.5):
        M[a]=j
    return M  
print M

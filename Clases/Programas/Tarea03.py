import math 

def Diana(x,y):
    if x>=5 and x<=25 and y<10:
        return(7)
    elif x>=5 and x<=25 and y>30:
        return(7)
    elif x<5 and y<=30 and y>=10:
        return(5)
    elif x>25 and y>=10 and y<=30:
        return(5)
    elif x<5 and y<10:
        return(3)
    elif x<5 and y>30:
        return(3)
    elif x>25 and y>30:
        return(3)
    elif x>25 and y<10:
        return(3)
    elif x>=5 and x<=25 and y<=30 and y>=10 and -525>= x**2 -10*x + y**2 -40*y:
        return(10)
    else:
        return(100)



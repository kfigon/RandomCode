__author__ = 'kamil'
def foo(a,b,c):
    delta = b**2 - 4*c*a

    if(delta == 0):
        return 1
    elif(delta < 0):
        return 0
    else:
        return 2


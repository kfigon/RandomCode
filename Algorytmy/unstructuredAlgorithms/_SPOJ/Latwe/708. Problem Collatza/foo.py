__author__ = 'kamil'
def foo(start):
    x = start
    n = 0
    while(x != 1):
        n+=1
        if(x % 2 == 1):
            x=3*x+1
        else:
            x = x/2

    return n
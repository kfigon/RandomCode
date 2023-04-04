__author__ = 'kamil'

def foo(a,b):
    if(a==b):
        return a+b

    if(a<b):
        return foo(a, b-a)
    else:
        return foo(a-b, b)
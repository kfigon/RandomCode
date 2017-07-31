__author__ = 'kamil'

def foo(podzielne, niepodzielne, granica):
    output = []

    for i in range(1, granica):
        if(i%podzielne == 0 and i % niepodzielne !=0):
            output.append(i)

    return output

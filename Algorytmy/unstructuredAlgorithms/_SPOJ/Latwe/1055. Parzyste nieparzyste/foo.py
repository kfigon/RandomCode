__author__ = 'kamil'
def foo(dane):
    output = []
    output += (bar(dane, 0))
    output += (bar(dane, 1))

    return output

def bar(dane, parzystyIndex):
    output = []
    for indeks, val in enumerate(dane):
        if((indeks+1) % 2 == parzystyIndex):
            output.append(val)

    return output
__author__ = 'kamil'

# Pierwszą cyfrę mnożymy przez 1,
# drugą cyfrę mnożymy przez 3,
# trzecią cyfrę mnożymy przez 7,
# czwarta cyfrę mnożymy przez 9,
# piątą cyfrę mnożymy przez 1,
# szóstą cyfrę mnożymy przez 3,
# siódmą cyfrę mnożymy przez 7,
# ósmą cyfrę mnożymy przez 9,
# dziewiątą cyfrę mnożymy przez 1,
# dziesiątą cyfrę mnożymy przez 3,
# jedenastą cyfrę mnożymy przez 1.
# Tak uzyskane 11 iloczynów dodajemy do siebie.
# Jeśli ostatnia cyfra tej sumy jest zerem to podany PESEL jest prawidłowy

def foo(pesel):
    if(len(pesel) != 11):
        return False
    suma = 0
    tab = [1,3,7,9,1,3,7,9,1,3,1]
    for i, cyfra in enumerate(pesel):
        suma += int(cyfra) * tab[i]

    return (suma % 10 == 0)

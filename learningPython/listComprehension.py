
lista = [i for i in range(10)]
print(lista)

parzystaLista = [i for i in range(20) if i % 2 ==0]
print(parzystaLista)

generator = (i for i in range(5))
print(generator)
print(list(generator))
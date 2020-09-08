def soma(*args):
    aux=0
    for valor in args:
        aux+= valor
    print (aux)

soma(2,4,6)

def f(**kwargs):
    print (kwargs)
    print (type(kwargs))


def contar_caracteres(s):
    """ Funcao que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('kelvin')
    {'e': 1, 'i': 1, 'k': 1, 'l': 1, 'n': 1, 'v': 1}

    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter==caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1

    resultado[caracter_anterior] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('kelvin'))
    print()
    print(contar_caracteres('banana'))

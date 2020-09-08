"Modulo que contem operacoes matematicas"

def soma(parcela, parcela_2):
    """ Funcao para calcular as parcelas

    :param parcela:
    :param parcela_2:
    :return:
    """
    return parcela + parcela_2

if __name__ == '__main__': #__name__ vai puxar o nome da funcao e comparar pra ver se esta sendo executada dentro do proprio modulo main de criacao
    print(soma(1,2))

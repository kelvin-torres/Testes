class Pessoa:
    def __init__ (self, *filhos, nome='Insira um nome', idade='none', sobrenome='insira um sobrenome'):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Ola Kelvin {id(self)}'


if __name__== '__main__':
    p = Pessoa()
    outroP = Pessoa('Ben, Sophie', nome='testando outro nome',)
    p.nome = 'tosco'
    p.idade = ''
    p.sobrenome = 'filhao'
    print(p.nome,p.idade,p.sobrenome)
    print(id(p.idade))
    print(Pessoa.comprimentar(p))
    #for filho in outroP.filhos:
    #    print(filho.nome)
    del p.sobrenome
    print(p.__dict__)
    print(outroP.__dict__)
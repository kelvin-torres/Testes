class Pessoa:
    def __init__ (self, nome='Insira um nome', idade='0', sobrenome='insira um sobrenome'):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

    def comprimentar(self):
        return f'Ola Kelvin {id(self)}'

if __name__== '__main__':
    p = Pessoa()
    p.nome = 'tosco'
    p.idade = ''
    p.sobrenome = 'filhao'
    print(p.nome,p.idade,p.sobrenome)
    print(id(p.idade))
    print(Pessoa.comprimentar(p))

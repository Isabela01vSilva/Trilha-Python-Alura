class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade 
        self.profissao = profissao 

    def __str__(self):
        return f'nome:{self.nome} | idade:{self.idade} | profissão: {self.profissao}' 
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('Jim', 33, 'Vendedor de papel')
pessoa2 = Pessoa('Pam', 30, 'Administradora')
pessoa3 = Pessoa('Angela', 40, 'Contadora')

print('Pessoas')
print(pessoa1)
print(pessoa2)
print(pessoa3)

pessoa1.aniversario()
pessoa3.aniversario()

print(f'\nFizeram Aniversario')
print(pessoa1)
print(pessoa2)
print(pessoa3)

print(f'\nSaudações')
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
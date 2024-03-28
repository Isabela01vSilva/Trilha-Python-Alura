class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #O title deixa as primeiras letrar em Maiúsculas 
        self._categoria = categoria.upper() #Upper deixa todas as letras em Maiúsculas
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        nome_restaurante = 'Nome do restaurante'
        categoria_restaurante = 'Categoria'
        print(f'{nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza place','Italiano')

Restaurante.listar_restaurantes()
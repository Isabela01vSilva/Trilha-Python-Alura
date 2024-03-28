from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #O title deixa as primeiras letrar em Maiúsculas 
        self._categoria = categoria.upper() #Upper deixa todas as letras em Maiúsculas
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        nome_restaurante = 'Nome do restaurante'
        categoria_restaurante = 'Categoria'
        media_restaurante = 'Avaliação'

        print(f'{nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(25)} | {media_restaurante.ljust(25)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5 :
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Não tem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_notas, 1)
        return media
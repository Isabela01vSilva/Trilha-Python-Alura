from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''Representa um restaurante e suas características.'''
    
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.'''
        
        self._nome = nome.title() #O title deixa as primeiras letrar em Maiúsculas 
        self._categoria = categoria.upper() #Upper deixa todas as letras em Maiúsculas
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''Retorna uma representação em string do restaurante.'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes.'''
        nome_restaurante = 'Nome do restaurante'
        categoria_restaurante = 'Categoria'
        media_restaurante = 'Avaliação'

        print(f'{nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(25)} | {media_restaurante.ljust(25)} | Status')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante.'''
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        '''Alterna o estado de atividade do restaurante.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        '''
        if 0 < nota <= 5 :
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        '''Calcula e retorna a média das avaliações do restaurante.'''
        if not self._avaliacao:
            return 'Não tem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

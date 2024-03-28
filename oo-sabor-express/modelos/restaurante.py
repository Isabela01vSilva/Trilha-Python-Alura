class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        nome_restaurante = 'Nome do restaurante'
        categoria_restaurante = 'Categoria'
        print(f'{nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(25)} | Status')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Place','Italiano')

Restaurante.listar_restaurantes()
#O 'dir()' mostrará tudo: os atributos, métodos e propriedades de um objeto
#print(dir(restaurante_praca))
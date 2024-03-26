class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Place','Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
#O 'dir()' mostrará tudo: os atributos, métodos e propriedades de um objeto
#print(dir(restaurante_praca))

#Exibi o que foi definido 
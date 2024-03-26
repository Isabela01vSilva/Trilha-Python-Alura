class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

#O 'dir()' mostrará tudo: os atributos, métodos e propriedades de um objeto
#print(dir(restaurante_praca))

#Exibi o que foi definido 
print(vars(restaurante_praca))
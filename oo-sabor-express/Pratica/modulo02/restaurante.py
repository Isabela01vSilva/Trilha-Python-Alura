print('\nMódulo 1: Instânicia de uma classe\n')

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante1 = Restaurante()
restaurante1.nome = 'Pizzaria'
restaurante1.categoria = 'Gourmet'
print(vars(restaurante1))

print('\n1. Atribua o valor Italiana em categoria ')
restaurante1.categoria = 'italiana'

print('\n2. Acessar o valor do atributo nome da instância')
nome = restaurante1.nome
print({nome})

print('\n3. Verificar o valor inicial do atributo ativo')
if  restaurante1.ativo == False:
    print('Restaurante está inativo')
else:
    print('Restaurante está ativo') 

print('\n4. Acessar o valor do atributo categoria')
categoria = restaurante1.categoria
print({categoria})

print('\n5. Alterar o valor do atributo nome para Bistrô')
restaurante1.nome = 'Bistrô'

print('\n6. Crie uma nova instância de classe Restaurante')
restaurante2 = Restaurante()
restaurante2.nome = 'Pizza Place'
restaurante2.categoria = 'Fast Food'
print(vars(restaurante2))

print('\n7. Verifique se a categoria da instância Pizza Place é Fast Food')
if restaurante2.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

print('\n8. Mude o estado da instância Pizza Plance para Ativo')
restaurante2.ativo = True
print(f'o restaurante {restaurante2.nome} está Ativo')
print('1. Imprimir uma frase')
print('Python na Escola de Programação da Alura\n')

print('2. Armazenar nome e idade')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos\n')

print('3. Imprimir uma palavra com as letras separadas')
print('A','L','U','R','A',sep='\n')

print('\n4. Imprimir o valor de pi')
pi_arredondado = 3.14159
print(f"O valor arredondado de pi é: {pi_arredondado:.2f}") 

print('\n 5. Exibir o tipo de genero')
def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Pop', 'Rock')
print(resultado)
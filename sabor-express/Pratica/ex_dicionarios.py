print('\nExercicios do Módulo 4: Dicionários\n')

print('1. Criando um Dicionário')
pessoa = {'nome': 'Isabela', 'idade': 22, 'cidade': 'São Paulo'}
print(f'{pessoa}\n')

print('2. Atualizando idade, Adicionando Profissão e Excluindo cidade')
# Atualização de Idade
pessoa['idade'] = 32
# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'
# Remoção de Elemento
del pessoa['cidade']
print(f'{pessoa}\n')

print('3. Criando um dicionário que apresenta os números de 1 a 5 e seus respectivos quadrados')
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(f'{numeros_quadrados}\n')

print('4. Verificando a existência de uma chave no dicionário')
pessoa = {'nome': 'Luiza', 'idade': 20, 'cidade': 'São Paulo'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.\n")
else:
    print("A chave 'nome' não existe no dicionário.\n")

print('5. Contando cada palavra em uma frase')
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

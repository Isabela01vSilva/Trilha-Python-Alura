print('Exercicios do Módulo 2: Condicionais\n')

def numero():
    print('1. Número ímpar ou par?')
    numero = int(input('Digite um numero: '))

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')

def idade():
    print('2. Criança, Adolescente ou Adulto?')
    idade = int(input('Qual sua idade? '))

    if idade <= 12:
        print(f'Você tem {idade}, é uma Criança')
    elif idade <= 18:
        print(f'Você tem {idade}, é Adolescente')
    elif idade > 18 :
        print(f'Você tem {idade}, é um Adulto')
    else:
        print('Valor inválido')

def acesso():
    print('3. Usuário e senha corretos?')

    usuario_correto = 'isabela'
    senha_correta = 123

    usuario = input('Digite seu usuario: ')
    senha = int(input('Digite sua senha: '))

    if usuario == usuario_correto and senha == senha_correta:
        print('Acessando...')
    else:
        print('Usuário ou senha incorretos')

def quadrante():
    print('4. Qual quadrante do plano cartesiano o ponto se encontra?') 

    x = float(input('Digite o valor de X: '))
    y = float(input('Digite o valor de y: '))

    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
        print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('Está no eixo ou origem')

def main():
    numero()
    idade()
    acesso()
    quadrante()

if __name__ == '__main__':
    main()
import os

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes_():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def encerrar_app():
    os.system('cls') 
    print('Encerrar o App\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    #opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1: 
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        encerrar_app()
    
def main():
    exibir_nome_do_programa()
    exibir_opcoes_()
    escolher_opcoes()

if __name__ == '__main__':
    main()
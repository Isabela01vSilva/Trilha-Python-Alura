import os

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa Função é responsavel por exibir o nome do programa'''

    print('Sabor Express\n')

def exibir_opcoes_():
    '''Essa Função é responsavel por exibir as opções do menu'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa Função é responsavel por exibir mensagem de finalização do programa'''

    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    '''Essa função solicita uma tecla para voltar ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''

    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''Essa Função é responsavel por verificar 
    se a opção que o usuario informou está correta 
    e voltar ao menu 
    
    Outputs:
    - Retorna ao menu principal
    '''
    
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa Função é responsavel por exibir um subtitulo
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa Função é responsavel por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria 

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dado_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dado_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa Função é responsavel por listar os restaurantes cadastrados
    
    Inputs: 
    - Nome do restaurante
    - Categoria 

     Outputs:
    - Exibe a lista de restaurantes na tela

    '''
    
    exibir_subtitulo('Listando restaurantes')
    
    nome_titulo = 'Nome do restaurante'.ljust(22)
    categoria_titulo = 'Categoria'.ljust(20)

    print(f'{nome_titulo} | {categoria_titulo} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_restaurantes():
    '''Essa Função é responsavel por alterar o estado ativo/desativado de um retaurante cadastrado
    
    Inputs: 
    - Nome do restaurante
    - Restaurante encontrado
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação

    '''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)  
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Essa Função é responsavel por solicita e executa a opção escolhida pelo usuário
    
    Funções: 
    - Cadastrar novo restaurante
    - Litar novo restaurante
    - Alterar novo restaurante
    - Finalizar programa
    - Opção invalida

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    ''' Função principal que inicia o programa '''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes_()
    escolher_opcoes()

if __name__ == '__main__':
    main()
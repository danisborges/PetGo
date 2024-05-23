import os

petshops = [{'nome':'Petshopinho', 'categoria':'Pequeno porte', 
             'ativo':False},
            {'nome':'BigPet', 'categoria':'Grande porte', 
             'ativo':True},
            {'nome':'PetFly', 'categoria':'Aves', 
             'ativo':False}]

def exibir_nome_do_programa():
  '''Esta função é responsável por apresentar o nome do programa'''
  print('PetGo​​​​​\n')

def exibir_opcoes():
    '''Esta função é responsável por exibir ao usuário as opções do menu'''
    print('MENU DE OPÇÕES')
    print('1. Cadastrar Petshop')
    print('2. Listar Petshops')
    print('3. Alternar status do Petshop')
    print('4. Sair\n')

def finalizar_app():
    '''Esta função é responsável por finalizar o app'''
    exibir_subtitulo('Finalizar app')

def voltar_menu_principal():
    '''Esta função é responsável por possibilitar o retorno ao menu'''
    input('\nDigite uma tecla para voltar ao menu principal.')
    main()

def opcao_invalida():
    '''Esta função é reponsável por informar ao usuário que a opção selecionada é inválida'''
    print('Opção inválida.\n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''Esta função é responsável por exibir os subtitulos em todas as etapas da aplicação'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# CRIANDO AS AÇÕES
def cadastrar_novo_petshop():
    '''Esta função é responsável por cadastrar um novo petshop
    
    Inputs:
    - Nome do petshop
    - Categoria

    Outputs:
    - Adiciona um novo petshop a lista de petshops
    
    '''
    exibir_subtitulo('Cadastro de novos Petshops\n')
    nome_petshop = input('Digite o nome do Petshop que deseja cadastrar: \n')
    categoria = input(f'Digite o nome da categoria do Petshop {nome_petshop}: ')
    dados_petshop = {'nome':nome_petshop, 'categoria':categoria, 'ativo': False}
    petshops.append(dados_petshop)
    print(f'\nPetshop {nome_petshop} cadastrado com sucesso!')

    voltar_menu_principal()

def listar_petshops():
    ''''''
    exibir_subtitulo('Listando petshops')
    
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')

    for petshop in petshops:
        nome_petshop = petshop['nome']
        categoria = petshop['categoria']
        ativo = 'ativado' if petshop['ativo'] else 'desativado'
        print(f'- {nome_petshop.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()
    
def alternar_status_petshop():
    exibir_subtitulo('Alternando estado do petshop.')
    nome_petshop = input('Digite o nome do petshop que deseja alternar o status: ')
    petshop_encontrado = False

    for petshop in petshops:
        if nome_petshop == petshop['nome']:
            petshop_encontrado = True
            petshop['ativo'] = not petshop['ativo']
            mensagem = f'O petshop {nome_petshop} foi ativado com sucesso' if petshop['ativo'] else f'O petshop foi desativado com sucesso!'
            print(mensagem)

    if not petshop_encontrado:
        print('O petshop não foi encontrado.')

    voltar_menu_principal()

# LISTAGEM DE OPÇÕES
def escolher_opcao():
    try: # tente fazer a conferência ..
        opcao_escolhida = int(input('Escolha uma opção: '))    
        
        if opcao_escolhida == 1:
            cadastrar_novo_petshop()
        elif opcao_escolhida == 2:
            listar_petshops()
        elif opcao_escolhida == 3:
            alternar_status_petshop()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: # caso não consiga, ...
        opcao_invalida()


def main(): # dita a ordem de execução de cada função
    os.system('cls') #limpa a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
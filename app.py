import os

restaurantes = [{'nome':'pizzo', 'categoria':'Pizzaria', 'ativo':False}, {'nome':'Sushi-San', 'categoria':'Japonesa', 'ativo':True},
                {'nome':'Churris', 'categoria':'churrasco', 'ativo': False}]

def exibir_nome_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes():
    '''Essa função mostra todas as opções do sistema'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza a aplicação'''
    os.system('cls')
    exibir_subtitilo('finalizando o app')

def exibir_subtitilo(texto):
    '''Essa função mostra a função escolhida'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função retorna a primeira tela da aplicação'''
    input('\ndigite uma tecla para voltar ao menu digital')
    main()

def opcao_invalida():
    '''Essa função chama outra funcção quando uma opção for inválida'''
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função cadastra novos restaurantes'''
    os.system('cls')
    exibir_subtitilo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurnate {nome_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista todos os restaurantes
    '''
    os.system('cls')
    exibir_subtitilo('Lista dos restaurantes')
    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função alterna o estado do restaurante de desativado para ativado e vice-versa'''
    exibir_subtitilo('Alternando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função mostra as opções do sistema para que o usuário escolha'''
    try:
        
        opcao_escolhida = int(input('Escolha uma opcão: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa é a função prinicpal da aplicação. A aplicação inicia nela'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



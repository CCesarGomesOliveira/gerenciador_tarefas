import os
tarefas = []
contador_tarefas = 0

def menu():
    os.system('cls')
    print('Bem-vindo(a) ao Tarefas!\n')
    print('Escolha uma das opções: ')
    print('1. Adicionar Tarefas')
    print('2. Visualizar Tarefas')
    print('3. Remover Tarefas')
    print('4. Sair ')
    escolher_opcao()

def adicionar_tarefas(titulo):
    
    global tarefas
    global contador_tarefas

    
    contador_tarefas = len(tarefas)
    exibir_subtitulo(titulo)
    while True:
        tarefas.append(str(input('\nDigite sua tarefa: ')))
        print(f'\n Tarefa - {tarefas[contador_tarefas]} - adicionada com sucesso')
        contador_tarefas +=1

        if input('deseja adicionar mais uma tarefa? digite "s" para sim ou qualquer tecla para voltar ') == 's':
            continue
        else:
            menu()
            break

def visualizar_tarefas(titulo):
    global tarefas
    global contador_tarefas

    contador_tarefas = 1

    exibir_subtitulo(f'{titulo}\n')

    if not tarefas:
        print('Não há nenhuma tarefa')
        while True:
            input('pressione enter para voltar ao menu')
            menu()
            break
    else:

        for tarefa in tarefas:
            print(f'{contador_tarefas} - {tarefa}')
            contador_tarefas +=1
        
        while True:
            input('pressione enter para voltar ao menu')
            menu()
            break

def remover_tarefas(titulo):
    global tarefas
    global contador_tarefas

    contador_tarefas = 1


    exibir_subtitulo(titulo)
    while True:
        remover_tarefa = input('deseja remover todas as tarefas? digite s/n: ')
        if remover_tarefa == 's':
            tarefas.clear()
            print('Todas as tarefas foram removidas')
            menu()
            return
        elif remover_tarefa == 'n':
            if not tarefas:
                print('Não há tarefas para remover.')
                while True:
                    input('pressione enter para voltar ao menu')
                    menu()
                    break   
        else:
            print('Por favor, digite "s/n"')
            continue

        
        for i, tarefa in enumerate(tarefas):
            print(f'{i + 1} - {tarefa}')

        while True:
            try:
                tarefa_excluir = int(input('selecione o número da tarefa para excluí-la: '))  
                indice_a_remover = tarefa_excluir - 1
                
                if 0 <= indice_a_remover < len(tarefas):
                    tarefa_removida = tarefas.pop(indice_a_remover)
                    print(f'Tarefa "{tarefa_removida}" removida com sucesso')
                    while True:
                        input('pressione enter para voltar ao menu')
                        menu()
                        break
                    break


                else:
                    print('Número de tarefa inválido. Tente novamente.')
                    continue
            except ValueError:
                print('Entrada inválida. Por favor, digite um número inteiro.')
                continue
                    

def sair(titulo):
    os.system('cls')
            

def exibir_subtitulo(tarefa_escolhida):
    os.system('cls')
    print(tarefa_escolhida)

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\n'))
    except ValueError:
        print('Por, digite o numero da opção')
        escolher_opcao()

    if opcao_escolhida == 1:
        adicionar_tarefas('Adicionando nova tarefa...')
    elif opcao_escolhida == 2:
        visualizar_tarefas('Visualizando tarefas...')
    elif opcao_escolhida == 3:
        remover_tarefas('Remover tarefa...')
    elif opcao_escolhida == 4:
        sair('saindo!')
    else:
        print('Opção Inválida')
        while True:
            input('pressione enter para voltar ao menu')
            menu()
            break
        

menu()
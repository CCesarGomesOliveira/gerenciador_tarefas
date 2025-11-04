'''
numero = int(input('Digite um número: \n'))

def verifica_par_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par!")
    else:
        print(f'{numero} é impar!')

verifica_par_impar(numero)
------------------------------------------------------------------------
'''

'''
idade = int(input('Type your age: '))

def classify_age(idade):
    if idade <= 12:
        print('Criança')
    elif idade <= 18:
        print('Adolescente')
    else:
        print('Adulto')

classify_age(idade)
-------------------------------------------------------------------------
'''
'''
coordenada_x = int(input('Digite a coordenada para o valor X (horizontal): '))
coordenada_y = int(input('Digite a coordenada para o valor y (vertical): '))

def determina_quadrante(x, y):
    x = coordenada_x
    y = coordenada_y

    if x > 0 and y > 0:
        print('primeiro quadrante')
    elif x < 0 and y > 0:
        print('segundo quadrante')
    elif x > 0 and y < 0:
        print('terceiro quadrante')
    elif x > 0 and y < 0:
        print('quarto quadrante')
    else:
        print('o ponto está localizado no eixo ou origem.')

determina_quadrante(coordenada_x, coordenada_y)
----------------------------------------------------------------------------
'''

'''numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = ["Maria", 'João', 'Ana', 'Carlos']

datas = [2008, 2025]

def calcula_impares():
    impares = []

    for num in numero:
        if num % 2 != 0:
            impares.append(num)
                    
    impares_calculados = sum(impares)
    print(impares_calculados)

calcula_impares()
----------------------------------------------------------------------------
'''

'''numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def imprime_decrescente():
    contador = 9
    for num in numero:
        print(num + contador)
        contador = contador - 2

imprime_decrescente()
------------------------------------------------------------------------------    
    '''

'''numero = int(input('Escolha um numero para ver sua tabuada: '))

def tabuada_numero(numero):
    contador = 1
    while contador <= 10: 
        tabuada = numero * contador
        contador += 1
        print(tabuada)

tabuada_numero(numero)
-------------------------------------------------------------------------
'''

'''numeros = [92, 15, 67, 4, 33, 89, 50, 22, 75, 11]
soma_numeros = []

try:
    for num in numeros:
        soma_numeros.append(num)
        numeros_somados = sum(soma_numeros)
    print(numeros_somados)
except Exception as e:
    print(f'Houve um erro: {e}')
--------------------------------------------------------------------------------    
'''


'''pessoa_infos = {'nome':'Cassiano', 'idade':16, 'cidade':'Ribeirão Preto'}

pessoa_infos['idade'] = 17
print(pessoa_infos['idade'])
del pessoa_infos['cidade']
print(pessoa_infos)
------------------------------------------------------------------------------
'''

'''numeros = {'2':2, '4':4, '8':8}
numeros_apenas = list(numeros.values())
numeros_quadrados = []
for num in numeros_apenas:
    numeros_quadrados.append(num ** 2)
print(numeros_apenas)
print(numeros_quadrados)
------------------------------------------------------------------------------
'''

'''def contar_frequencia_palavras(frase):
    frase = frase
    contagem_palavras = {}
    palavras = frase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)

contar_frequencia_palavras('Não há nada melhor que Jesus Sim Jesus')
-----------------------------------------------------------------------------------
'''
'''
def compara_desempenho_produtos():
    qtd_maca = int(input('quantas maçãs foram vendidas?'))    
    qtd_bananas = int(input('quantas bananas foram vendidas?'))

    if qtd_maca > qtd_bananas:
        print('As maçãs venderam mais!')    
    elif qtd_maca < qtd_bananas:
        print('As bananas venderam mais!')
    else:
        print('ambas venderam a mesma quantidade!')    

compara_desempenho_produtos()
--------------------------------------------------------------'''
'''
def calcula_tempo_total():
    dias_atividade_a = int(input('Informe os dias para a atividade A: '))
    dias_atividade_b = int(input('Informe os dias para a atividade B: '))
    dias_atividade_c = int(input('Informe os dias para a atividade C: '))

    if dias_atividade_a <0 or dias_atividade_b <0 or dias_atividade_c <0:
        print('ERRO: Os dias não podem ser negativos')
    else:
        print('aguarde o processamente...')

calcula_tempo_total()
---------------------------------------------------------------------------'''

'''def calcula_imc():
    peso = float(input('Informe seu peso em KG: '))
    altura = (float(input('Informe sua altura em metros: ')))

    imc = (peso / (altura ** 2))

    if imc < 18.5:
        print(f'\nvocê esta abaixo do peso - seu imc: {imc}')
    elif imc < 25:
        print(f'\nseu peso está normal - seu imc: {imc}')
    else:
        print(f'\nvocê está acima do peso - seu imc {imc}')

calcula_imc()
----------------------------------------------------------------------'''
'''def monitora_orcamento():
    salario = float(input('Informe seu salário: '))
    limite_orçamento = float(input('Informe até quanto você quer gastar: '))

    ha_despesa = True
    despesas = []
    total_despesas = []

    while ha_despesa == True:
        despesa = float(input('informe sua despesa: '))
        despesas.append(despesa)
        mais_despesa = str(input('Há mais despesas? digite s/n: '))

        if mais_despesa == 'n':
            ha_despesa = False
            print(f'suas despesas foram: {despesas}')
            total_despesas = sum(despesas)
            print(f'\nno total, seus gastos foram {total_despesas}')
            
            if total_despesas > limite_orçamento:
                print('passou do limite, hein!')
            else:
                print('Está no limite!')
       

monitora_orcamento()'''


'''def calcula_media():
    notas = []
    adiciona_notas = True
    contador = 1

    while adiciona_notas == True:
        notas.append(int(input(f'Digite a nota {contador}: ')))
        mais_notas = input('adicionar mais uma nota? digite s/n: ')
        if mais_notas == 's':
            contador += 1
        else:
            adiciona_notas = False
            media = (sum(notas)) / len(notas)

            print(f'\nA média é: {media}')
            if media >= 7:
                        print('\nAprovado!')
            elif media >= 5:
                        print('\nRecuperação!')
            else:
                        print('\nReprovado!')

       


calcula_media()
-------------------------------------------------------------------
'''

'''def somar_valores():   
    valores = [10, 20, 30, 40, 50]
    soma_total = 0

    for valor in valores:
        soma_total += valor
    print(f'a soma é: {soma_total}')
    


somar_valores()
--------------------------------------------------------------------------------------------------------------------------------'''

'''projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

def printa_projetos():
    for pj in projetos:
        if pj == None:
            print('projeto ausente')
            continue
        print(f'projeto: {pj}')

printa_projetos()
----------------------------------------------------------------------------------------------------------------------------------'''

'''livros_estoque = [{'titulo':'O Peregrino', 'autor':'John Bunyan', 'ano':1678, 'estoque':5}, {'titulo':'Confissões', 'autor':'Agostinho de Hipona', 'ano':397, 'estoque':5}, {'titulo':'Uma Vida com Propósitos', 'autor':'Rick Warren', 'ano':2002, 'estoque':5}]

def comprar_livro():
    contador = 1
    print(f'Qual livro deseja comprar\n')
    for livro in livros_estoque:
        print(f'{contador}. {livro['titulo']} - {livro['estoque']}')
        contador +=1

    
    comprar_mais = True

    while comprar_mais == True:
        livro_selecionado = input('\ndigite o nome do livro: ')
        for livro in livros_estoque:
            if livro['titulo'] == livro_selecionado:
                livro['estoque'] -= 1
                if livro['estoque'] <= 0:
                    print('Esgotado')
                    break
                print(f'{livro['titulo']} - {livro['estoque']}')
                decisao = input('quer comprar mais? s/n: ')
                if decisao == 'n':
                    comprar_mais = False
            
        



comprar_livro()
-------------------------------------------------------------------------------------------------------------'''

'''livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] <= 0:
        print(f'esgotado: {livro['nome']}')
        continue
    print(f'Livro disponivel: {livro['nome']}')
    ------------------------------------------------------------------------------------------------------'''

'''
produtos = input('digite cada produto separado por ,: ').split(',')
valores = input('digite cada valor separado por ,: ').split(',')

for produto, valor in zip(produtos, valores):
     print(f"{produto.strip()}: {valor.strip()}")

result = list(zip(produtos, valores))
print(result)
--------------------------------------------------------------------------------------------------------'''



''''soma = lambda num_1, num_2: num_1 + num_2 

subtracao =  lambda num_1, num_2: num_1 - num_2 

multplicacao =  lambda num_1, num_2: num_1 * num_2 

divisao =  lambda num_1, num_2: num_1 / num_2


num_1 = int(input('Escolha o primeiro numero: '))
num_2 = int(input('Escolha o segundo numero: '))
operador = input('Escolha + | - | * | / : ')

if operador == '+':
    print(soma(num_1, num_2))
elif operador == '-':
    print(subtracao(num_1, num_2))
elif operador == '*':
    print(multplicacao(num_1, num_2))
else:
    print(divisao(num_1, num_2))


--------------------------------------------------------------------------------------------------------------------'''

'''def sistema_desconto(porcentagem):

    def aplica_desconto(valor):
        return valor - (valor * (porcentagem / 100))

    return aplica_desconto
    
    
desconto = float(input('digite a porcentagem: '))

calculadora_desconto = sistema_desconto(desconto)

valor = float(input("Digite o valor da compra: "))  

print(f'\n {calculadora_desconto(valor)}')
---------------------------------------------------------------------'''



'''def acumulados(n):
   if n == 1:
      return 1
   return n + acumulados(n - 1)
    

escolha = int(input('escolha um numero: '))

acumulados(escolha)
 
print(f'A soma de 1 a {escolha} é: {acumulados(escolha)}')
------------------------------------------------------'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
         return fibonacci(n-1) + fibonacci(n-2)
    
termo = int(input("Digite qual termo da sequência de Fibonacci você quer (ex: 6): "))

print(f"O {termo}º termo de Fibonacci é: {fibonacci(termo)}")
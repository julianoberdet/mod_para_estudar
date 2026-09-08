from controle_estoque_v1_0.lib.interface import *
from controle_estoque_v1_0.lib.arquivo import *
from time import sleep

arq = 'estoque.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar todos os produtos','Cadastrar novo produto','Buscar produto por código',
                     'Registrar Saída/Entrada de Estoque','Sair do Sistema'])
    if resposta == 1:
        listarProdutos(arq)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        cod = leiaInt('Código: ')
        nome = leiaStr('Produto: ')
        preco = leiaFloat('Preço:R$ ')
        qtd = leiaInt('Quantidade de estoque: ')
        cadastrarNovo(arq,cod,nome,preco,qtd)

    elif resposta == 3:
        cod = leiaInt('Código para buscar: ')
        buscaProduto(arq,cod)

    elif resposta == 4:
        cod = leiaInt('Código do Produto: ')
        tipo = leiaStr('Entrada ou saida?[E/S] ').upper()[0]
        qtd = leiaInt('Quantidade? ')
        if tipo == 'S':
            qtd = -qtd
        registrarMovimento(arq,cod,qtd)

    elif resposta == 5:
        print('\n\033[32mSaindo do sistema',end='')
        for _ in range(3):
            sleep(1)
            print('.',end='',flush=True)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1)
print(' Ate a próxima!!\033[m')

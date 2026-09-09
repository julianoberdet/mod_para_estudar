from controle_estoque_v1_0.lib.interface import *
from controle_estoque_v1_0.lib.arquivo import *
from time import sleep

arq = 'estoque.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar todos os produtos','Cadastrar novo produto','Buscar produto por código',
                     'Registrar Entrada de Estoque (Reposição)','Realizar venda do Produto (Baixa no Estoque)',
                     'Deletar Produto','Sair do Sistema'])
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
        cabeçalho('ENTRADA NO ESTOQUE')
        cod = leiaInt('Código do Produto: ')
        qtd = leiaInt('Quantidade de entrada: ')
        registrarEntrada(arq,cod,qtd)

    elif resposta == 5:
        cabeçalho('VENDA DE PRODUTO')
        cod = leiaInt('Código do Produto: ')
        qtd = leiaInt('Quantidade vendida: ')
        realizarVenda(arq,cod,qtd)

    elif resposta == 6:
        cod = leiaInt('Código para deletar: ')
        conf = leiaStr(f'Tem certeza que quer deletar {cod}?[S/N] ').upper()[0]
        if conf == 'S':
            deletarProduto(arq,cod)

    elif resposta == 7:
        print('\n\033[32mSaindo do sistema',end='')
        for _ in range(3):
            sleep(1)
            print('.',end='',flush=True)
        break

    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1)
print(' Ate a próxima!!\033[m')

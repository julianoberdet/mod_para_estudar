from controle_estoque_v1_0.lib.interface import *
from os import write


def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} foi criado')


def listarProdutos(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabeçalho('Produtos cadastrados')
        print(f'{"Cod":<6} | {"Nome":<22} | {"Preço(R$)":>12} | {"Qtd Estoque":>12}')
        print(linha())
        for l in a:
            dado = l.split(';')
            dado[3] = dado[3].replace('\n','')
            print(f'{dado[0]:<6} | {dado[1]:<22} | {dado[2]:>12} | {dado[3]:>12}')
    finally:
        a.close()


def cadastrarNovo(arq,cod=0,nome='desc',preco=0.0,qtd=0):
    try:
        a = open(arq,'at')
    except:
        print('\033[mHouve um erro na abertura dos dados\033[m')
    else:
        try:
            a.write(f'{cod} ; {nome} ; {f"{preco:.2f}".replace('.',',')} ; {qtd}\n')
        except:
            print('\033[31mHouve um erro para escrever dados\033[m')
        else:
            print(f'Novo registro {nome} adicionado')
            a.close()


def buscaProduto(arq,codigo):
    try:
        with open(arq,'rt') as a:
            for l in a:
                dados = l.strip().split(';')
                # dados = [cod,nome,preco,qtd]
                if int(dados[0]) == codigo:
                    cabeçalho(f'PRODUTO ENCONTRADO: {codigo}')
                    preco_limpo = dados[2].strip().replace(',','.')
                    print(f"cod: {dados[0]}  |  Nome: {dados[1].strip()}  "
                        f"|  Preço: R${float(preco_limpo):.2f}"
                        f"|  Estoque: {dados[3]}")
                    return True
        print('\033[31mERRO!Código não encontrado.\033[m')
        return False
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado.\033[m')


def registrarMovimento(arq,codigo,qtd_mov):
    #qtd_mov positivo = entrada, geativo = saida
    lista = []
    achou = False
    try:
        with open(arq,'rt') as a:
            for l in a:
                dados = l.strip().split(';')
                if int(dados[0]) == codigo:
                    achou = True
                    estoque_atual = int(dados[3])
                    novo_estoque = estoque_atual + qtd_mov

                    if novo_estoque < 0:
                        print(f'\033[31mERRO! Estoque insuficiente.Só tem {estoque_atual}\033[m')
                        return False

                    dados[3] = str(novo_estoque)
                    print(f'\033[31mSucesso! {dados[1]}:{estoque_atual} -> {novo_estoque}\033[m')
                    if novo_estoque < 10:
                        print(f'\033[31mALERTA! estoque baixo de {dados[1]}\033[m')
                lista.append(';'.join(dados) + '\n')
        if not achou:
            print('\033[31mCódigo não existe\033[m')
            return False

        #Reescreve o arquivo inteiro atualizado
        with open(arq,'wt') as a:
            a.writelines(lista)
        return True
    except Exception as e:
        print(f'ERRO: {e}')
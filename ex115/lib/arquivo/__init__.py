from os import write
from ex115.lib.interface import *
def ArquivoExiste(nome):
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
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro na abertura dos dados')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro para escrever dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        print(f'{"Nome":<30}{"Idade":>3}')
        print(linha(42))
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:.<30}{dado[1]:>3} anos')
    finally:
        a.close()


def excluirCadastro(arq,nome):
    try:
        #Lê todos da lista
        with open(arq,'rt') as a:
            linhas = a.readlines()

        #Procura quem tem aquele nome
        novo = []
        achou = False
        for l in linhas:
            dados= l.split(';')
            nome_arquivo = dados[0].strip()
            if nome_arquivo.lower() == nome.lower().strip():
                achou = True
            else:
                novo.append(l)

        if not achou:
            print(f'ERRO! Nome {nome} não encontrado')
            return

        #Reescreve o arquivo sem aquela pessoa
        with open(arq,'wt') as a:
            a.writelines(novo)

        print(f'Nome {nome} removido com sucesso!')

    except Exception as erro:
        print(f'ERRO! a excluir: {erro}')
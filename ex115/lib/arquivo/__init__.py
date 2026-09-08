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
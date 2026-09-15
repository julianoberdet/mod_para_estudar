from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not ArquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas','Excluir pessoa','Sair do sistema'])
    if resp == 1:
        LerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resp == 3:
        LerArquivo(arq)
        print()
        cabecalho('EXCLUIR PESSOA')
        nomeExcluir = str(input('Qual nome deseja excuir? ')).strip()
        excluirCadastro(arq,nomeExcluir)

    elif resp == 4:
        print(linha())
        print('\033[36mSaindo do sistema',end='')
        for _ in range(3):
            print('.',end='')
            sleep(1)
        print('\nAté Logo!\033[m')
        print(linha())
        break
    else:
        print('ERRO! Digite uma opção válida')
    sleep(2)


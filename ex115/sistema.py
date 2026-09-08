from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not ArquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas','Sair do sistema'])
    if resp == 1:
        LerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resp == 3:
        cabecalho('\033[33m      Saindo do sistema... Até Logo!\033[m')
        break
    else:
        print('ERRO! Digite uma opção válida')
    sleep(2)


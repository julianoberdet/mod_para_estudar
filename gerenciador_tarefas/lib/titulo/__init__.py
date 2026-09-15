import sys
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu sair do sistema\033[m')
            print(linha())
            sys.exit()
        else:
            return n



def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for l in lista:
        print(f'\033[36m{c}\033[m - \033[33m{l}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[36mSua opção:\033[m ')
    return opcao
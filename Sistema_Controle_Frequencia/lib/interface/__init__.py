import sys
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print('ERRO: Digite um número inteiro')
        except KeyboardInterrupt:
            print('\nO usuário preferiu sair')
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
        print(f'\033[1;34m{c}\033[m - \033[1;32m{l}\033[m')
        c +=1
    print(linha())
    opc= leiaInt('\033[1;34mSua opção:\033[m ')
    return opc

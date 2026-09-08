import sys
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: Digite um número válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar dados!\033[m')
            sys.exit()
        else:
            return n


def leiaFloat(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()

        # Trata entrada vazia ou formato inválido
        if entrada == '' or entrada.isalpha():
            print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[m')
            continue

        try:
            return float(entrada)
        except (ValueError,TypeError):
            print('\033[31mERRO: Digite um número válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar dados!\033[m')
            sys.exit()


def leiaStr(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            if n == '':
                print('\033[31mERRO!Não pode ser vazio\033[m')
                continue

            #tem que ter pelo menos 1 letra, impede só número: "500"
            tem_letra = any(c.isalpha() for c in n)

            #permite letra,número e espaço, bloqueia @#$%¢ etc
            #Dipirona 500mg -> ok
            #"500" -> bloqueia(sem letra)
            #Dipiron@ -> bloqueia (tem simbolo)
            valido = all(c.isalnum() or c.isspace() for c in n)

            if not tem_letra or not valido:
                print('\033[31mERRO! Digite um produto válido')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            sys.exit()
        else:
            return n



def linha(tam=60):
    return '=' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu(lista):
    cabeçalho('CONTROLE DE ESTOQUE v1.0')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Qual opção? ')
    return opc
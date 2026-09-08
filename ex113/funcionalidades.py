def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: Digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: Digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n
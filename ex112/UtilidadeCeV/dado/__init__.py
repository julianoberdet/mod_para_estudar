import sys
def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()

        # Trata entrada vazia ou formato inválido
        if entrada == '' or entrada.isalpha():
            print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[m')
            continue

        try:
            return float(entrada)
        except ValueError:
            print(f'\033[1;31mERRO! "{entrada}" não é um valor monetário válido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu cancelar a entrada de dados.\033[m')
            sys.exit()




#Jeito sem tratamento de erro
'''def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)'''
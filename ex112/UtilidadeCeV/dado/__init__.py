import sys
def leiaDinheiro(msg):
    while True:
        try:
            num = str(input(msg)).replace(',','.').strip()
            return float(num)
        except ValueError:
            print(f'\033[1;31mERRO! \"{num}\" não é um valor monetário\033[m')
        except KeyboardInterrupt:
            print('\nO usuario prefiriu sair')
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
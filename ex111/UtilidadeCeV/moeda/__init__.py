def moeda(preco=0.0, moeda_simbolo='R$'):
    return f'{moeda_simbolo}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0.0, taxa=0.0, formata=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if not formata else moeda(resultado)


def diminuir(preco=0.0, taxa=0.0, formata=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if not formata else moeda(resultado)


def dobro(preco=0.0, formata=False):
    resultado = preco * 2
    return resultado if not formata else moeda(resultado)


def metade(preco=0.0, formata=False):
    resultado = preco / 2
    return resultado if not formata else moeda(resultado)


def resumo(preco=0.0, aum=0.0, dim=0.0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aum}% de aumento: \t{aumentar(preco, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(preco, dim, True)}')
    print('-' * 30)
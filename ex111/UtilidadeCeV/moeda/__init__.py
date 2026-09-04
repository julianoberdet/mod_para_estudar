def aumentar(preco,taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco,taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def moeda(preco,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco,aum,dim):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(preco,aum))}')
    print(f'{dim}% de redução: \t{moeda(diminuir(preco,dim))}')
    print('-' *30)
def moeda(preco,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def aumentar(preco,taxa,log=False):
    res = preco + (preco * taxa/100)
    return res if log is False else moeda(res)


def diminuir(preco,taxa,log=False):
    res = preco - (preco * taxa/100)
    return res if log is False else moeda(res)


def dobro(preco,log=False):
    res = preco * 2
    return res if log is False else moeda(res)


def metade(preco,log=False):
    res = preco / 2
    return res if log is False else moeda(res)


def resumo(preco,aum,dim):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'A metade do preço: \t{metade(preco,True)}')
    print(f'{aum}% de aumento: \t{aumentar(preco,aum,True)}')
    print(f'{dim}% de redução: \t{diminuir(preco,dim,True)}')
    print('-' *30)
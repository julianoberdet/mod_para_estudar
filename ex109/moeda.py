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


def moeda(preco,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

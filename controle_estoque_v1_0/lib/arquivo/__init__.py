from controle_estoque_v1_0.lib.interface import cabeçalho, linha

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'\033[31mHouve um erro ao criar o arquivo: {e}\033[m')
    else:
        print(f'Arquivo {nome} foi criado com sucesso!')


def listarProdutos(nome):
    try:
        with open(nome, 'rt') as a:
            cabeçalho('Produtos Cadastrados')
            print(f'{"Cod":<6} | {"Nome":<22} | {"Preço(R$)":>12} | {"Qtd Estoque":>12}')
            print(linha())
            for l in a:
                if not l.strip():
                    continue  # Ignora linhas vazias
                dado = [item.strip() for item in l.split(';')]
                if len(dado) >= 4:
                    print(f'{dado[0]:<6} | {dado[1]:<22} | {dado[2]:>12} | {dado[3]:>12}')
    except Exception as e:
        print(f'\033[31mERRO ao ler o arquivo: {e}\033[m')


def cadastrarNovo(arq, cod=0, nome='desc', preco=0.0, qtd=0):
    try:
        with open(arq, 'at') as a:
            preco_str = f"{preco:.2f}".replace('.', ',')
            a.write(f'{cod};{nome};{preco_str};{qtd}\n')
            print(f'Novo registro "{nome}" adicionado com sucesso!')
    except Exception as e:
        print(f'\033[31mHouve um erro ao escrever os dados: {e}\033[m')


def buscaProduto(arq, codigo):
    try:
        with open(arq, 'rt') as a:
            for l in a:
                if not l.strip():
                    continue
                dados = [item.strip() for item in l.split(';')]
                if int(dados[0]) == codigo:
                    cabeçalho(f'PRODUTO ENCONTRADO: {codigo}')
                    preco_limpo = dados[2].replace(',', '.')
                    print(f"Cod: {dados[0]}  |  Nome: {dados[1]}  "
                          f"|  Preço: R${float(preco_limpo):.2f}  "
                          f"|  Estoque: {dados[3]}")
                    return True
        print('\033[31mERRO! Código não encontrado.\033[m')
        return False
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado.\033[m')


def registrarEntrada(arq, codigo, qtd_entrada):
    lista = []
    achou = False
    try:
        with open(arq, 'rt') as a:
            for l in a:
                if not l.strip():
                    continue
                dados = [item.strip() for item in l.split(';')]
                if int(dados[0]) == codigo:
                    achou = True
                    estoque_atual = int(dados[3])
                    novo_estoque = estoque_atual + qtd_entrada
                    dados[3] = str(novo_estoque)
                    print(f'\033[32mReposição efetuada! {dados[1]}: {estoque_atual} -> {novo_estoque}\033[m')
                lista.append(';'.join(dados) + '\n')

        if not achou:
            print('\033[31mCódigo não encontrado!\033[m')
            return False

        with open(arq, 'wt') as a:
            a.writelines(lista)
        return True
    except Exception as e:
        print(f'\033[31mERRO ao registrar entrada: {e}\033[m')


def realizarVenda(arq, codigo, qtd_vendida):
    lista = []
    achou = False
    try:
        with open(arq, 'rt') as a:
            for l in a:
                if not l.strip():
                    continue
                dados = [item.strip() for item in l.split(';')]
                if int(dados[0]) == codigo:
                    achou = True
                    estoque_atual = int(dados[3])
                    preco = float(dados[2].replace(',', '.'))

                    if qtd_vendida > estoque_atual:
                        print(f'\033[31mERRO! Estoque insuficiente! Estoque atual: {estoque_atual}\033[m')
                        return False

                    total_venda = preco * qtd_vendida
                    novo_estoque = estoque_atual - qtd_vendida
                    dados[3] = str(novo_estoque)

                    print(linha())
                    print(f'VENDA REALIZADA: {dados[1]}'.center(60))
                    print(f'Qtd: {qtd_vendida} x R${preco:.2f} = R${total_venda:.2f}'.center(60))
                    print(f'Estoque: {estoque_atual} -> {novo_estoque}'.center(60))
                    print(linha())

                    if novo_estoque < 10:
                        print(f'\033[33mALERTA! Estoque baixo de {dados[1]}: {novo_estoque} unidade(s)\033[m')

                lista.append(';'.join(dados) + '\n')

        if not achou:
            print('\033[31mCódigo não encontrado!\033[m')
            return False

        with open(arq, 'wt') as a:
            a.writelines(lista)
        return True
    except Exception as e:
        print(f'\033[31mERRO ao realizar venda: {e}\033[m')


def deletarProduto(arq, cod):
    lista = []
    achou = False
    try:
        with open(arq, 'rt') as a:
            for l in a:
                if not l.strip():
                    continue
                dados = [item.strip() for item in l.split(';')]
                if int(dados[0]) == cod:
                    achou = True
                    print(f'\033[31mProduto "{dados[1]}" removido com sucesso!\033[m')
                    continue
                lista.append(';'.join(dados) + '\n')

        if not achou:
            print('\033[31mCódigo não encontrado!\033[m')
            return False

        with open(arq, 'wt') as a:
            a.writelines(lista)
        return True
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m')
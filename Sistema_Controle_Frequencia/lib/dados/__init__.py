from Sistema_Controle_Frequencia.lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq,'rt',encoding='utf-8')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq,'wt+',encoding='utf-8')
    except:
        print('Erro ao criar o arquivo')
    else:
        print(f'Arquivo {arq} foi criado')
        a.close()


def cadastrarAluno(arq,matricula=0,nome='desconhecido',faltas=0):
    try:
        a = open(arq,'at',encoding='utf-8')
        a.write(f'{matricula};{nome};{faltas}\n')
    except:
        print('Houve um erro para cadastrar aluno')
    else:
        print(f'Aluno {nome} foi cadastrado com {faltas} faltas')
        a.close()


def listarAlunos(arq):
    cabeçalho('LISTAGEM DE ALUNOS')
    print(f'{"MAT.":<5} {"ALUNO":<30} {"FALTAS":>8}')
    print(linha())
    try:
        a = open(arq, 'rt', encoding='utf-8')
    except:
        print('Houve um erro para ler o arquivo')
    else:
        try:
            for l in a:
                dado = l.replace('\n', '').split(';')
                if len(dado) == 3:
                    print(f'{dado[0]:<5}  {dado[1]:<30}  {dado[2]:>8}')
        finally:
            a.close()


def cadastrar_nova_Falta(arq, cod=0):
    lista = []
    achou = False
    nome_alterado = ''  # 1. CRIA A VARIÁVEL AQUI FORA

    try:
        with open(arq, 'rt', encoding='utf-8') as a:
            for l in a:
                dado = l.replace('\n', '').split(';')
                if len(dado) == 3:
                    mat, nome, faltas = dado[0], dado[1], int(dado[2])

                    if int(mat) == cod:
                        achou = True
                        nome_alterado = nome  # 2. SALVA O NOME CERTO AQUI DENTRO
                        print(f'Aluno encontrado: {nome} (Faltas atuais: {faltas})')

                        while True:
                            nova = leiaInt('Quantidade de faltas a adicionar: ')
                            if nova >= 0:
                                break
                            print('\033[31mERRO: O número de faltas deve ser maior ou igual a zero!\033[m')

                        total_de_faltas = faltas + nova
                        lista.append(f'{mat};{nome};{total_de_faltas}\n')
                    else:
                        lista.append(f'{mat};{nome};{faltas}\n')
    except FileNotFoundError:
        print('ERRO: Arquivo de presenças não encontrado')
    except Exception as erro:
        print(f'Houve um erro ao ler o arquivo: {erro}')
        return

    if not achou:
        print(f'ERRO! Matrícula {cod} não encontrada no sistema')
    else:
        try:
            with open(arq, 'wt', encoding='utf-8') as a:
                a.writelines(lista)
                # 3. USA A VARIÁVEL COM O NOME TRAVADO AQUI
                print(f'\033[36mFaltas de {nome_alterado} atualizadas com sucesso\033[m')
        except:
            print('Houve um erro ao atualizar o arquivo')





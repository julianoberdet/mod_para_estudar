from gerenciador_tarefas.lib.titulo import *
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
        a =  open(arq,'wt+',encoding='utf-8')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {arq} foi criado')


def cadastrarTarefa(arq, tarefa='desconhecido', status='desconhecido'):
    try:
        a = open(arq, 'at', encoding='utf-8')
        a.write(f'{tarefa};{status}\n')
    except:
        print('Houve um erro ao cadastrar a tarefa.')
    else:
        print(f"Registro de '{tarefa}' adicionado com sucesso!")
    finally:
        a.close()


def lerTarefa(arq, status_filtro=None):
    # Ajusta o título do cabeçalho de acordo com o filtro aplicado
    titulo = 'TAREFAS CADASTRADAS' if not status_filtro else f'TAREFAS ({status_filtro.upper()})'
    cabeçalho(titulo)

    print(f'{"ID":<5} {"TAREFA":<34} {"STATUS":<10}')
    print(linha())

    try:
        a = open(arq, 'rt', encoding='utf-8')
    except:
        print('Houve um erro ao ler o arquivo.')
    else:
        c = 1
        for l in a:
            dado = l.replace('\n', '').split(';')
            if len(dado) == 2:
                tarefa_nome, status_atual = dado[0], dado[1]

                # Se status_filtro for definido, só imprime se for igual ao status da linha
                if status_filtro is None or status_atual.lower() == status_filtro.lower():
                    print(f'\033[35m{c:<5}\033[m{tarefa_nome:<34}{status_atual:<10}')
                    c += 1
    finally:
        a.close()
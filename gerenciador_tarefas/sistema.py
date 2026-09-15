from gerenciador_tarefas.lib.titulo import *
from gerenciador_tarefas.lib.dados import *
from time import sleep

arq = 'tarefas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver tarefas cadastradas','Cadastrar nova tarefa','Sair do sistema'])
    if resposta == 1:
        lerTarefa(arq)

    elif resposta == 2:

        cabeçalho('NOVA TAREFA')
        descricao_tarefa = str(input('Descrição da tarefa: '))
        status = leiaInt('Status da tarefa:[1]Pendente/[2]Concluída ')
        if status == 1:
            status = 'Pendente'
        elif status == 2:
            status = 'Concluída'
        else:
            print('Houve um erro ao cadastrar o status')
            continue
        cadastrarTarefa(arq,descricao_tarefa,status)

    elif resposta == 3:
        print(linha())
        print('\033[36mSaindo do sistema',end='')
        for _ in range(3):
            print('.',end='')
            sleep(1)
        print('\nATÉ A PRÓXIMA!\033[m')
        print(linha())
        break
    else:
        print('ERRO: Digite uma opção válida do menu')
    sleep(2)
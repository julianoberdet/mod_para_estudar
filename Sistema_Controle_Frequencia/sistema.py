from Sistema_Controle_Frequencia.lib.interface import *
from Sistema_Controle_Frequencia.lib.dados import *
from time import sleep

arq = 'Frequencia.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar alunos e faltas','Cadastrar novo aluno','Registrar nova falta',
                     'Excluir cadastro','Sair do sistema'])
    if resposta == 1:
        listarAlunos(arq)

    elif resposta == 2:
        cabeçalho('NOVO ALUNO')
        matricula = leiaInt('Matricula: ')
        nome = str(input('Nome: '))
        cadastrarAluno(arq,matricula,nome)

    elif resposta == 3:
        # 1. Exibe a lista para o usuário visualizar as matrículas
        listarAlunos(arq)  # Ou o nome da sua função de listagem

        # 2. Leitura e validação da matrícula
        mat_busca = leiaInt('\nDigite a matrícula do aluno: ')

        # 3. Execução do registro
        cadastrar_nova_Falta(arq, mat_busca)

    elif resposta == 4:
        listarAlunos(arq)
        cabeçalho('EXCLUIR ALUNO')
        cod_Matricula = leiaInt('\nDigite a Matricula do aluno para excluir: ')
        excluirAluno(arq,cod_Matricula)

    elif resposta == 5:
        print(linha())
        print('\033[1;31mSaindo do sistema',end='')
        for _ in range(3):
            print('.',end='')
            sleep(1)
        print('\nMUITO OBRIGADO, ATÉ LOGO!\033[m')
        print(linha())
        break
    else:
        cabeçalho('ERRO: Digite uma opção válida')
    sleep(2)
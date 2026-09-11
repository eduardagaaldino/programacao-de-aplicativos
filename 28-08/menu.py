from banco import tabela_escolas, tabela_turmas, tabela_alunos
from escola import cadastrar_escolas, listar_escolas, atualizar_escolas, excluir_escolas
from turmas import cadastrar_turmas, listar_turmas, atualizar_turmas, excluir_turmas
from alunos import cadastrar_alunos, listar_alunos, atualizar_alunos, excluir_alunos

def menu_escolas():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar escolas")
            print("2- listar escolas ")
            print("3- atualizar escolas ")
            print("4- excluir escolas ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_escola = input("digite o nome da escola que deseja cadastrar:")
                cidade_escola = input("digite a cidade em que a escola esta localizada:")
                banco = 'gestao_escolar.db'
                cadastrar_escolas(nome_escola, cidade_escola, banco)

            elif opcao == 2:
                banco = 'gestao_escolar.db'
                listar_escolas(banco)
            
            elif opcao == 3:
                id_escola = int(input("Digite o ID da escola que deseja alterar: "))
                novo_nome_escola = input("digite o novo nome da escola:")
                nova_cidade_escola = input("digite a nova cidade:")
                banco = 'gestao_escolar.db'
                atualizar_escolas(id_escola , novo_nome_escola , nova_cidade_escola , banco)

            elif opcao == 4:
                id_escola = int(input("Digite o ID da escola que deseja excluir: "))
                banco = 'gestao_escolar.db'
                excluir_escolas(id_escola , banco)

            else:
                break

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

def menu_turmas():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar turmas")
            print("2- listar turmas ")
            print("3- atualizar turmas ")
            print("4- excluir turmas ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_turma = input("digite o nome da turma que deseja cadastrar:")
                id_escola = input("digite o id da escola que esta vinculada a turma:")
                banco = 'gestao_escolar.db'
                cadastrar_turmas(nome_turma, id_escola, banco)

            elif opcao == 2:
                banco = 'gestao_escolar.db'
                listar_turmas(banco)
            
            elif opcao == 3:
                id_turma = int(input("Digite o ID da turma que deseja alterar: "))
                novo_nome_turma = input("digite o novo nome da turma:")
                novo_id_escola = input("digite o id da nova escola vinculada:")
                banco = 'gestao_escolar.db'
                atualizar_turmas(id_turma , novo_nome_turma , novo_id_escola , banco)

            elif opcao == 4:
                id_turma = int(input("Digite o ID da turma que deseja excluir: "))
                banco = 'gestao_escolar.db'
                excluir_turmas(id_turma , banco)

            else:
                break

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")


def menu_alunos():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar alunos")
            print("2- listar alunos ")
            print("3- atualizar alunos ")
            print("4- excluir alunos ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                nome_aluno = input("digite o nome do aluno que deseja cadastrar:")
                idade_aluno = int(input("digite a idade do aluno que deseja cadastrar:"))
                id_turma = input("digite o id da turma que esse aluno esta vinculado:")
                banco = 'gestao_escolar.db'
                cadastrar_alunos(nome_aluno, idade_aluno, id_turma, banco)

            elif opcao == 2:
                banco = 'gestao_escolar.db'
                listar_alunos(banco)
            
            elif opcao == 3:
                id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
                novo_nome_aluno = input("digite o novo nome do aluno:")
                nova_idade_aluno = input("digite a nova idade do aluno:")
                novo_id_turma = input("digite o id da nova turma vinculada:")
                banco = 'gestao_escolar.db'
                atualizar_alunos(id_aluno , novo_nome_aluno, nova_idade_aluno, novo_id_turma , banco)

            elif opcao == 4:
                id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
                banco = 'gestao_escolar.db'
                excluir_alunos(id_aluno, banco)

            else:
                break

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

def menu():
    try:
        opcao = 0

        while opcao != 4:
            print("---------------------------------------------")
            print("1- escolas")
            print("2- turmas ")
            print("3- alunos ")
            print("4- sair ")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                menu_escolas()

            elif opcao == 2:
                menu_turmas()
            
            elif opcao == 3:
                menu_alunos()

            else:
                break

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

menu()
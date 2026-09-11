import sqlite3

def cadastrar_alunos(nome_aluno, idade_aluno, id_turma ,banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        comando_inserir = (f'''INSERT INTO alunos
                            (nome_aluno,idade_aluno, id_turma)
                            VALUES ('{nome_aluno}', '{idade_aluno}', '{id_turma}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("aluno cadastrado!")

    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:    
        conexao.close()


def listar_alunos(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        conexao.close()

        print("\n--- alunos ---")

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(
                    f"ID: {aluno[0]} | "
                    f"Nome: {aluno[1]} | "
                    f"idade: {aluno[2]} |"
                    f"turma: {aluno[3]} "
                )

    except sqlite3.Error:
        print(f"Erro ao listar alunos")

def atualizar_alunos(id_aluno, novo_nome_aluno, nova_idade_aluno, novo_id_turma, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE alunos
        SET nome_aluno = '{novo_nome_aluno}',
            idade_aluno = '{nova_idade_aluno}',
            id_turma = '{novo_id_turma}'
        WHERE id_aluno = {id_aluno}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("aluno atualizado com sucesso!")
        else:
            print("Nenhum aluno foi encontrado com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_alunos(id_aluno , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM alunos WHERE id_aluno = {id_aluno}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print ("aluno excluído com sucesso!")
        else:
            print ("Nenhum aluno foi encontrado com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

# def menu_alunos():
#     try:
#         opcao = 0

#         while opcao != 5:
#             print("---------------------------------------------")
#             print("1- cadastrar alunos")
#             print("2- listar alunos ")
#             print("3- atualizar alunos ")
#             print("4- excluir alunos ")
#             print("5- sair")
#             opcao = int(input("escolha uma das opcoes a cima: "))
#             print("---------------------------------------------")

#             if opcao == 1:
#                 nome_aluno = input("digite o nome do aluno que deseja cadastrar:")
#                 idade_aluno = int(input("digite a idade do aluno que deseja cadastrar:"))
#                 id_turma = input("digite o id da turma que esse aluno esta vinculado:")
#                 banco = 'gestao_escolar.db'
#                 cadastrar_alunos(nome_aluno, idade_aluno, id_turma, banco)

#             elif opcao == 2:
#                 banco = 'gestao_escolar.db'
#                 listar_alunos(banco)
            
#             elif opcao == 3:
#                 id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
#                 novo_nome_aluno = input("digite o novo nome do aluno:")
#                 nova_idade_aluno = input("digite a nova idade do aluno:")
#                 novo_id_turma = input("digite o id da nova turma vinculada:")
#                 banco = 'gestao_escolar.db'
#                 atualizar_alunos(id_aluno , novo_nome_aluno, nova_idade_aluno, novo_id_turma , banco)

#             elif opcao == 4:
#                 id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
#                 banco = 'gestao_escolar.db'
#                 excluir_alunos(id_aluno, banco)

#     except ValueError:
#         print("Erro: digite apenas numeros!")
#     finally:
#         print("------------------------------------------------")
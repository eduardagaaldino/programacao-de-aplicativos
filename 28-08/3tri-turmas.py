import sqlite3

def cadastrar_turmas(nome_turma, id_escola ,banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        comando_inserir = (f'''INSERT INTO turmas
                            (nome_turma, id_escola)
                            VALUES ('{nome_turma}', '{id_escola}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("turma cadastrado!")

    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:    
        conexao.close()


def listar_turmas(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        print("\n--- turmas ---")

        if not turmas:
            print("Nenhuma turma cadastrada.")
        else:
            for turma in turmas:
                print(
                    f"ID: {turma[0]} | "
                    f"Nome: {turma[1]} | "
                    f"Cidade: {turma[2]}"
                )

    except sqlite3.Error:
        print(f"Erro ao listar turmas")

def atualizar_turmas(id_turma, novo_nome_turma, novo_id_escola, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE turmas
        SET nome_turma = '{novo_nome_turma}',
            id_escola = '{novo_id_escola}'
        WHERE id_turma = {id_turma}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("turma atualizada com sucesso!")
        else:
            print("Nenhuma turma foi encontrada com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_turmas(id_turma , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM turmas WHERE id_turma = {id_turma}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print ("turma excluída com sucesso!")
        else:
            print ("Nenhuma turma foi encontrada com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

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

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")

menu_turmas()
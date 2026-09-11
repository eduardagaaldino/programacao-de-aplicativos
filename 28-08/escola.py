import sqlite3

def cadastrar_escolas(nome_escola, cidade_escola ,banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO escolas
                        (nome_escola, cidade_escola)
                        VALUES ('{nome_escola}', '{cidade_escola}')''')

        conexao.commit()
        conexao.close()

        return("Escola cadastrada com sucesso!")

    except sqlite3.Error:
        print(f"Erro ao cadastrar escola")


def listar_escolas(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        print("\n--- ESCOLAS ---")

        if not escolas:
            print("Nenhuma escola cadastrada.")
        else:
            for escola in escolas:
                print(
                    f"ID: {escola[0]} | "
                    f"Nome: {escola[1]} | "
                    f"Cidade: {escola[2]}"
                )

    except sqlite3.Error:
        print(f"Erro ao listar escolas")

def atualizar_escolas(id_escola, novo_nome_escola, nova_cidade_escola, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE escolas
        SET nome_escola = '{novo_nome_escola}',
            cidade_escola = '{nova_cidade_escola}'
        WHERE id_escola = {id_escola}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            return("escola atualizado com sucesso!")
        else:
            return("Nenhuma escola foi encontrada com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def excluir_escolas(id_escola , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM escolas WHERE id_escola = {id_escola}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "escola excluída com sucesso!"
        else:
            return "Nenhuma escola foi encontrada com esse ID."

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

# def menu_escolas():
#     try:
#         opcao = 0

#         while opcao != 5:
#             print("---------------------------------------------")
#             print("1- cadastrar escolas")
#             print("2- listar escolas ")
#             print("3- atualizar escolas ")
#             print("4- excluir escolas ")
#             print("5- sair")
#             opcao = int(input("escolha uma das opcoes a cima: "))
#             print("---------------------------------------------")

#             if opcao == 1:
#                 nome_escola = input("digite o nome da escola que deseja cadastrar:")
#                 cidade_escola = input("digite a cidade em que a escola esta localizada:")
#                 banco = 'gestao_escolar.db'
#                 cadastrar_escolas(nome_escola, cidade_escola, banco)

#             elif opcao == 2:
#                 banco = 'gestao_escolar.db'
#                 listar_escolas(banco)
            
#             elif opcao == 3:
#                 id_escola = int(input("Digite o ID da escola que deseja alterar: "))
#                 novo_nome_escola = input("digite o novo nome da escola:")
#                 nova_cidade_escola = input("digite a nova cidade:")
#                 banco = 'gestao_escolar.db'
#                 atualizar_escolas(id_escola , novo_nome_escola , nova_cidade_escola , banco)

#             elif opcao == 4:
#                 id_escola = int(input("Digite o ID da escola que deseja excluir: "))
#                 banco = 'gestao_escolar.db'
#                 excluir_escolas(id_escola , banco)

#     except ValueError:
#         print("Erro: digite apenas numeros!")
#     finally:
#         print("------------------------------------------------")
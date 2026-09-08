
import sqlite3
from banco import conectar

def cadastrar_escola(nome, cidade ,banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar escola: {erro}")


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

    except sqlite3.Error as erro:
        print(f"Erro ao listar escolas: {erro}")

def atualizar_redes(id_escola, novo_nome_escola, novo_cidade_escola, banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE redes_diagnosticos
        SET nome_grupo = '{novo_nome_rede}',
            sac = '{novo_sac}'
        WHERE id_rede = {id_rede}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("rede atualizado com sucesso!")
        else:
            print("Nenhuma rede foi encontrada com esse ID!")

        return "rede atualizada!"

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

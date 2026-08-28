import sqlite3 
 
def tabela_escolas(banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS escolas(
                        id_escola INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_escola TEXT NOT NULL,
                        cidade_escola TEXT NOT NULL
                        )''')

        conexao.commit()
        return "tabela escolas criada!"

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    finally:    
        conexao.close()


def tabela_turmas (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS turmas(
                        id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_turma TEXT NOT NULL,
                        id_escola INTEGER,
                        FOREIGN KEY (id_escola) REFERENCES escolas(id_escola)
                        )''')
    
        conexao.commit()
        return"tabela turmas criada!"

    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

def tabela_alunos (banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS alunos(
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_aluno TEXT NOT NULL,
                        idade_aluno TEXT NOT NULL,
                        id_turma INTEGER,
                        FOREIGN KEY (id_turma) REFERENCES turmas (id_turma)
                        )''')

        conexao.commit()
        return"tabela alunos criada!"

    except sqlite3.Error:
        print("Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 


banco = "gestao_escolar.db"
mensagem1 = tabela_escolas(banco)
mensagem2 = tabela_turmas(banco)
mensagem3 = tabela_alunos(banco)

print(mensagem1)
print(mensagem2)
print(mensagem3)

# banco = "teste_gestao_escolar.db"
# assert tabela_escolas(banco) == "tabela escolas criada!"
# assert tabela_turmas(banco) == "tabela turmas criada!"
# assert tabela_alunos(banco) == "tabela alunos criada!"
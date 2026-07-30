#se o id_prof nao existir, ocorre um integrityerror
#se o erro acontecer, o que ocorre com a linha conexao.close()?

#faltava o try, except e finally, que faz o codigo rodar mesmo ouver um erro



import sqlite3

def criar_tabela_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_serie INTEGER,
            id_prof INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_prof) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute('''
            INSERT INTO turmas (nome, id_serie, id_prof)
            VALUES (?, ?, ?)
        ''', (nome, id_serie, id_prof))

        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: professor ou série não existe.")

    finally:
        conexao.close()

criar_tabela_turmas()

cadastrar_turma("Turma A", 1, 1)
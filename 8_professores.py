#O sistema aceita cadastrar dois professores com o mesmo CPF.
#Como restringir isso direto na estrutura da tabela abaixo?

#faltava um UNIQUE no text



import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS professores
    """)

    cursor.execute("""
    CREATE TABLE professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL
    )
    """)

    conexao.commit()

    cursor.execute("""
    INSERT INTO professores (nome, cpf)
    VALUES (?, ?)
    """, ("Moya", "000000000"))

    conexao.commit()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("Lista de Professores:")
    for professor in professores:
        print(professor)

    conexao.close()

cadastrar_professor("Moya", "0000000000")  


# o python reclama de "incorrect number of bindings"
# estamos passando a variavel, por que ocorre o erro?

#e presciso por uma virgula no final dp id_prof



import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf UNIQUE TEXT
        )
    ''')

    conexao.commit()
    cursor.execute(
        "SELECT nome FROM professores WHERE id = ?",
        (id_prof,)
    )


    resultado = cursor.fetchone()

    if resultado:
        print("Professor encontrado:", resultado[0])
    else:
        print("o professor não foi encontrado!")

    conexao.close()

buscar_professor(1)   
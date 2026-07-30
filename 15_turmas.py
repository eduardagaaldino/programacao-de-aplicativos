import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema.escola_db')
    cursor = conexao.curso()

    #O SQLITE ACUSA O ERRO DE SINTAXE PRÓXIMO AO FOREN KEY. CADÊ O ERRO?
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS turmas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomr_turma TEXT, 
                id_serie,
                FOREIGN KEY (id_serie) REFERENCES serie(id)
                )
                ''')
    conexao.commit()
    conexao.close()

#faltava o () do conexao.cursor(), E avia um erro na escrita  FOREIGN
import sqlite3

def cadastrar_turma(nome,id_serie,id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_keys = ON;")

        #se o id_prof nao existir, ocorre um integrityerror
        #se o erro acontecer, o que ocorre com a linha conexao.close()?
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)"), (nome , id_serie , id_prof)
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor ou série não existe.")
    finally:
        conexao.close()

#faltava o try, except e finally, que faz o codigo rodar mesmo ouver um erro

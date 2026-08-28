import sqlite3

def cadastrar_escolas():
    try: 
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        comando_inserir = (f'''INSERT INTO escolas
                            (nome_escola, cidade_escola)
                            VALUES('{nome_escola}', '{cidade_escola}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        return "escola cadastrada!"

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    finally:    
        conexao.close()

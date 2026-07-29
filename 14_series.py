import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    
    try:
        #SE A LINHA ABAIXO FALHAR POR FALTA DE PERMISSÃO NA PASTA,
        #O BLOCO 'FINALLY' VAI TENTAR FECHAR ALGO QUE NÃO ABIU. COMO CORRIGIR?
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))
        conexao.commit()
    except sqlite3.Error as e:
        print("Erro técnico:", e)
    finally:
        if conexao is not None:
            conexao.close()

#faltava verificar se a conexao nao estava vazia
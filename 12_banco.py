import sqlite3

# O aluno criou a conexão fora das funções para "facilitar".
# Por que isso quebra o sistema quando usamos multiplos arquivos (módulos)?

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSER INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit()

#a conexao deve ser criada dentro da def para evitar a criacao de varios modulos 
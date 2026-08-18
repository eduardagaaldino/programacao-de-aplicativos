import sqlite3

def verficar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    #PORQUE O SEGUNDO PRINT NÃO MOSTRA ABSOLUTAMENTE NADA NO CONSOLE?
    dados = cursor.fetchall():
    print("Primeiro print:", dados)
    print("Segundo print:", dados)

    conexao.close()

#pq o fetchall so roda uma vez
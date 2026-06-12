print("----------banco de dados escola----------")

import sqlite3

def cadastrar()
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute ('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_completo TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
                )''')

nome = input("digite o nome completo do aluno:")
telefone = input("digite o telefone do aluno:")
turma = input("digite a turma do aluno:")
idade = int(input("digite a idade do aluno:"))
cpf = input("digite o cpf do aluno:")

comando_inserir = (f'''
                    INSERT INTO alunos (nome_completo , telefone , turma , idade , cpf)
                    VALUES ('{nome}' , '{telefone}' , '{turma}' , {idade} , '{cpf}')''')

cursor.execute(comando_inserir)
conexao.commit()
print("cadastrado")
conexao.close()



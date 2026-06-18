print("\n=====professores=====")


import sqlite3

def criar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario TEXT,
                    escola TEXT
                    )''')


    nome = input("digite o nome completo do professor:")
    telefone = input("digite o telefone do professor:")
    materia = input("digite a materia do professor:")
    idade = int(input("digite a idade do professor:"))
    cpf = input("digite o cpf do professor:")
    salario = input("digite o salario do professor: R$")
    escola = input("digite a escola em que o professor esta trabalhando:")

    comando_inserir = (f'''
                        INSERT INTO * FROM professores
                        ''')

    cursor.execute(comando_inserir)
    conexao.commit()
    print("cadastrado")
    conexao.close()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM professores''')

    professores = cursor.fetchall()


    print("\n=== PROFESSORES CADASTRADOS ===\n")

    if not professores:
        print("nunhum professor cadastrado!")
    else:    
        for P in professores:
            print(f"ID: {P[0]}")
            print(f"Nome: {P[1]}")
            print(f"Telefone: {P[2]}")
            print(f"materia: {P[3]}")
            print(f"Idade: {P[4]}")
            print(f"CPF: {P[5]}")
            print(f"salario: {P[6]}")
            print(f"escola: {P[7]}")
            print("-" * 40)

    conexao.close()

def alterar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_professor = int(input("Digite o ID do professor que deseja alterar: "))
    novo_nome = input("digite o novo  nome completo do professore:")
    novo_telefone = input("digite o novo telefone do professore:")
    nova_materia = input("digite a nova materia do professore:")
    nova_idade = int(input("digite a nova idade do professore:"))
    novo_cpf = input("digite o novo cpf do professore:")
    novo_salario = input("digite o novo salario do professor: R$")
    nova_escola = input("digite a nova escola em que o professor esta trabalhando:")


    sql = f'''
    UPDATE professores
    SET nome = '{novo_nome}',
        telefone = '{novo_telefone}',
        materia = '{nova_materia}',
        idade = '{nova_idade}',
        cpf = '{novo_cpf}',
        salario = '{novo_salario}',
        escola = '{nova_escola}'
    WHERE id = {id_professor}
    '''

    cursor.execute(sql)

    conexao.commit()

    if cursor.rowcount > 0:
        print("professor atualizado com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")

    conexao.close()

def remover():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_professor = int(input("Digite o ID do professor que deseja excluir: "))

    sql = f'''DELETE FROM professores WHERE id = {id_professor}'''

    cursor.execute(sql)
    conexao.commit()

    if cursor.rowcount > 0:
        print("professor excluído com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")

    conexao.close()

def menu():
    opcao = 0

    while opcao != 5:
        print(25 * "-")
        print("1- cadastrar")
        print("2- listar ")
        print("3- alterar ")
        print("4- remover ")
        print("5- sair")
        print(25 * "-")
        opcao = int(input("escolha uma das opcoes a cima: "))

        if opcao == 1:
            criar()

        elif opcao == 2:
            listar()
        
        elif opcao == 3:
            alterar()

        elif opcao == 4:
            remover()
    print("programa encerrao!")
    print("------------------------------")

menu()
import sqlite3

def criar_professor():
    try: 
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS professores(
                        id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_professor TEXT NOT NULL,
                        telefone_professor TEXT,
                        materia_professor TEXT,
                        idade_professor INTEGER,
                        cpf_professor TEXT UNIQUE NOT NULL,
                        salario_professor TEXT,
                        escola_professor TEXT,
                        endereco_professor TEXT
                        )''')


        nome = input("digite o nome completo do professor:")
        telefone = input("digite o telefone do professor:")
        materia = input("digite a materia do professor:")
        idade = int(input("digite a idade do professor:"))
        cpf = input("digite o cpf do professor:")
        salario = input("digite o salario do professor: R$")
        escola = input("digite a escola em que o professor esta trabalhando:")
        endereco = input("digite o endereco do professor: ")

        comando_inserir = (f'''INSERT INTO professores 
                            (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, escola_professor, endereco_professor)
                            VALUES('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', '{salario}', '{escola}', '{endereco}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("cadastrado")

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    except ValueError:
        print("Erro: a idade deve aver apenas numeros!")

    except sqlite3.IntegrityError:
        print("erro: essa informacao ja existe!")

    finally:    
        conexao.close()

def listar_professores():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM professores''')

        professores = cursor.fetchall()


        print("\n=== PROFESSORES CADASTRADOS ===")

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
                print(f"endereco: {P[8]}")
                print("-" * 40)

    except IndexError:
        print("Erro: posicao nao encontrada")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

def alterar_professor():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        id_professor = int(input("Digite o ID do professor que deseja alterar: "))
        novo_nome = input("digite o novo  nome completo do professor:")
        novo_telefone = input("digite o novo telefone do professor:")
        nova_materia = input("digite a nova materia do professor:")
        nova_idade = int(input("digite a nova idade do professor:"))
        novo_cpf = input("digite o novo cpf do professor:")
        novo_salario = input("digite o novo salario do professor: R$")
        nova_escola = input("digite a nova escola em que o professor esta trabalhando:")
        novo_endereco = input("digite o novo do professor:")


        sql = f'''
        UPDATE professores
        SET nome_professor = '{novo_nome}',
            telefone_professor = '{novo_telefone}',
            materia_professor = '{nova_materia}',
            idade_professor = '{nova_idade}',
            cpf_professor = '{novo_cpf}',
            salario_professor = '{novo_salario}',
            escola_professor = '{nova_escola}',
            endereco_professor = '{novo_endereco}'
        WHERE id_professor = {id_professor}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("professor atualizado com sucesso!")
        else:
            print("Nenhum professor encontrado com esse ID.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def remover_professor():
    try:
        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        id_professor = int(input("Digite o ID do professor que deseja excluir: "))

        sql = f'''DELETE FROM professores WHERE id_professor = {id_professor}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print("professor excluído com sucesso!")
        else:
            print("Nenhum professor encontrado com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

def menu_professores():
    try:
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
                criar_professor()

            elif opcao == 2:
                listar_professores()
            
            elif opcao == 3:
                alterar_professor()

            elif opcao == 4:
                remover_professor()

    except ValueError:
        print("Erro: digite apenas numeros!")

    finally:
        print("programa encerrado!")
        print("------------------------------")

def criar_aluno():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS alunos(
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_aluno TEXT NOT NULL,
                        telefone_aluno TEXT,
                        turma_aluno TEXT,
                        idade INTEGER,
                        cpf_aluno TEXT UNIQUE NOT NULL,
                        id_professor INTEGER,
                        endereco_aluno TEXT,
                        cidade_aluno TEXT,
                        estado_aluno TEXT,
                        FOREIGN KEY (id_professor) REFERENCES professores(id)
                        )''')

        nome = input("digite o nome completo do aluno:")
        telefone = input("digite o telefone do aluno:")
        turma = input("digite a turma do aluno:")
        idade = int(input("digite a idade do aluno:"))
        cpf = input("digite o cpf do aluno:")
        endereco = input("digite o endereco do aluno:")
        cidade = input("digite a cidade do aluno:")
        estado = input("digite o estado do aluno:")

        comando_inserir = (f'''INSERT INTO alunos
                            (nome_aluno, telefone_aluno, turma_aluno, idade, cpf_aluno, endereco_aluno, cidade_aluno, estado_aluno)
                            VALUES('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', '{endereco}', '{cidade}', '{estado}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("aluno cadastrado!")

    except sqlite3.IntegrityError:
        print("erro: essa informacao ja existe!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:    
        conexao.close()

def listar_alunos():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM alunos''')

        alunos = cursor.fetchall()


        print("\n=== ALUNOS CADASTRADOS ===\n")

        if not alunos:
            print("nunhum aluno cadastrado!")
        else:    
            for aluno in alunos:
                print(f"ID: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Telefone: {aluno[2]}")
                print(f"Turma: {aluno[3]}")
                print(f"Idade: {aluno[4]}")
                print(f"CPF: {aluno[5]}")
                print(f"endereco: {aluno[6]}")
                print(f"cidade: {aluno[7]}")
                print(f"estado: {aluno[8]}")
                print("-" * 40)

    except IndexError:
        print("Erro: posicao nao encontrada")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

def alterar_aluno():
    try:
        conexao = sqlite3.connect('escola_demonstracao.db')
        cursor = conexao.cursor()

        id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
        novo_nome = input("Digite o novo nome: ")
        novo_cpf = input("Digite o novo CPF: ")

        sql = f'''
        UPDATE Alunos
        SET nome_aluno = '{novo_nome}',
            cpf_aluno = '{novo_cpf}'
        WHERE id_aluno = {id_aluno}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("Aluno atualizado com sucesso!")
        else:
            print("Nenhum aluno encontrado com esse ID.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()

def remover_aluno():
    try:
        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

        sql = f"DELETE FROM Alunos WHERE id_aluno = {id_aluno}"

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Aluno excluído com sucesso!")
        else:
            print("Nenhum aluno encontrado com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()

def menu_alunos():
    try:
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
                criar_aluno()

            elif opcao == 2:
                listar_alunos()
            
            elif opcao == 3:
                alterar_aluno()

            elif opcao == 4:
                remover_aluno()

    except ValueError:
        print("Erro: digite apenas numeros!")

    finally:
        print("programa encerrado!")
        print("------------------------------")

def menu_principal():
    try:
        opcao_escolha = 0

        while opcao_escolha != 3:
            print("-----sistema escolar-----")
            print("1-professores")
            print("2-alunos")
            print("3-sair")
            opcao_escolha = int(input("escolha uma das opcoes a cima:"))
            print("-------------------------")

            if opcao_escolha == 1:
                menu_professores()

            elif opcao_escolha == 2:
                menu_alunos()

    except ValueError:
            print("Erro: digite apenas numeros!")

    finally:
        print("prograna encerrado!")
        print("-----------------------------")

menu_professores()
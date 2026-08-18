import sqlite3

def cadastrar_hospital():
    try:

        conexao = sqlite3.connect('sistema_hospital.db')
        cursor = conexao.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS hospital (
                        id_hospital INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                        nome_hospital TEXT NOT NULL,
                        cidade_hospital TEXT NOT NULL
                        )
                        '''
                        )
        nome_hospital = input("\nDigite qual o nome do hospital: ") 
        cidade_hospital = input("Digite a cidade que está localizado o hospital: ")

        comando_inserir = f'''INSERT INTO hospital (nome_hospital, cidade_hospital)
                            VALUES('{nome_hospital}','{cidade_hospital}')'''
        print ("Hospital cadastrado com sucesso!")

        cursor.execute(comando_inserir)
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    finally:    
        conexao.close()

cadastrar_hospital()

def cadastrar_medico():
    try:
    
        conexao = sqlite3.connect('sistema_hospital.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        conexao.execute('''
                        CREATE TABLE IF NOT EXISTS medico (
                        id_medico INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                        nome_medico TEXT NOT NULL,
                        crm_medico INTEGER UNIQUE NOT NULL,
                        id_hospital INTEGER UNIQUE,
                        FOREIGN KEY (id_hospital) REFERENCES hospital(id_hospital)
                        )
                        '''                    
                        )
        nome_medico = input("\nDigite qual o seu nome: ")
        crm_medico = input("Digite qual o seu CRM: ")
        id_hospital = input("Qual o ID do seu hospital: ")

        comando_inserir = f'''INSERT INTO medico (nome_medico, crm_medico, id_hospital)
                            VALUES ('{nome_medico}','{crm_medico}','{id_hospital}')'''
        print("medico cadstrado com sucesso!")
        cursor.execute(comando_inserir)
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.IntegrityError:
        print("erro: essa informacao ja existe!")

    finally:
        conexao.close()

cadastrar_medico()
#Sistema de Laboratório de Exames 
#Tabela principal: redes_diagnostico (id, nome_grupo, sac) 
#Tabela dependente: laboratorios (id, cidade, id_rede -> vincula a redes_diagnostico) 

import sqlite3

def cadastrar_redes():
    try: 
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS redes_diagnosticos(
                        id_rede INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_grupo TEXT NOT NULL,
                        sac TEXT NOT NULL
                        )''')


        nome_grupo = input("digite o nome do grupo:")
        sac = input("digite o SAC:")

        comando_inserir = (f'''INSERT INTO redes_diagnosticos 
                            (nome_grupo , sac)
                            VALUES('{nome_grupo}', '{sac}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("rede de exames cadastrada!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    finally:    
        conexao.close()



def listar_redes():
    try:
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM redes_diagnosticos''')

        redes_diagnosticos = cursor.fetchall()


        print("\n=== REDES CADASTRADAS ===")

        if not redes_diagnosticos:
            print("nunhuma rede cadastrada!")
        else:    
            for r in redes_diagnosticos:
                print(f"ID: {r[0]}")
                print(f"Nome: {r[1]}")
                print(f"SAC: {r[2]}")
                print("------------------------------------------")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()



def atualizar_redes():
    try:
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        id_rede = int(input("Digite o ID da rede que deseja alterar: "))
        novo_nome_grupo = input("digite o novo nome do grpo:")
        novo_sac = input("digite o novo SAC:")

        sql = f'''
        UPDATE redes_diagnosticos
        SET nome_grupo = '{novo_nome_grupo}',
            sac = '{novo_sac}'
        WHERE id_rede = {id_rede}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("rede atualizado com sucesso!")
        else:
            print("Nenhuma rede foi encontrada com esse ID!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()



def excluir_redes():
    try:
        conexao = sqlite3.connect("laboratirio_exames.db")
        cursor = conexao.cursor()

        id_rede = int(input("Digite o ID da rede que deseja excluir: "))

        sql = f'''DELETE FROM redes_diagnosticos WHERE id_rede = {id_rede}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print("rede excluído com sucesso!")
        else:
            print("Nenhuma rede foi encontrada com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()



def menu_redes():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar redes")
            print("2- listar redes ")
            print("3- atualizar redes ")
            print("4- excluir redes ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                cadastrar_redes()

            elif opcao == 2:
                listar_redes()
            
            elif opcao == 3:
                atualizar_redes()

            elif opcao == 4:
                excluir_redes()

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")


def cadastrar_laboratorios ():
    try:
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS laboratorios(
                        id_laboratorio INTEGER PRIMARY KEY AUTOINCREMENT,
                        endereco_laboratorio TEXT NOT NULL,
                        id_rede INTEGER,
                        FOREIGN KEY (id_rede) REFERENCES redes_diagnosticos(id_rede)
                        )''')

        endereco_laboratorio = input("digite o endereco do laboratorio:")
        id_rede = int(input("digite o ID da rede em que o laboratorio esta inserido:"))
    
        comando_inserir = (f'''INSERT INTO laboratorios
                            (endereco_laboratorio, id_rede)
                            VALUES ('{endereco_laboratorio}', '{id_rede}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        print("laboratorio cadastrado!")

    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:    
        conexao.close()



def listar_laboratorios():
    try:
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM laboratorios''')

        laboratorios = cursor.fetchall()

        print("\n=== LABORATORIOS CADASTRADOS ===\n")

        if not laboratorios:
            print("nenhum laboratorio cadastrado!")
        else:    
            for l in laboratorios:
                print(f"ID: {l[0]}")
                print(f"endereco: {l[1]}")
                print(f"rede: {l[2]}")
                print("----------------------------------------")


    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()




def atualizar_laboratorios():
    try:
        conexao = sqlite3.connect('laboratirio_exames.db')
        cursor = conexao.cursor()

        id_laboratorio= int(input("Digite o ID do laboratorio que deseja atualizar: "))
        novo_endereco = input("Digite o novo endereco: ")

        sql = f'''
        UPDATE laboratorios
        SET endereco_laboratorio = '{novo_endereco}'
        WHERE id_laboratorio = {id_laboratorio}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("laboratorio atualizado com sucesso!")
        else:
            print("Nenhum laboratorio foi encontrado com esse ID.")

    except sqlite3.Error:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()




def excluir_laboratorios():
    try:
        conexao = sqlite3.connect("laboratirio_exames.db")
        cursor = conexao.cursor()

        id_laboratorio = int(input("Digite o ID do laboratorio que deseja excluir: "))

        sql = f"DELETE FROM laboratorios WHERE id_laboratorio = {id_laboratorio}"

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            print("laboratorio excluído com sucesso!")
        else:
            print("Nenhum laboratorio foi  encontrado com esse ID.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()



def menu_laboratorios():
    try:
        opcao = 0

        while opcao != 5:
            print("---------------------------------------------")
            print("1- cadastrar laboratorios")
            print("2- listar laboratorios ")
            print("3- atualizar laboratorios ")
            print("4- excluir laboratorios ")
            print("5- sair")
            opcao = int(input("escolha uma das opcoes a cima: "))
            print("---------------------------------------------")

            if opcao == 1:
                cadastrar_laboratorios()

            elif opcao == 2:
                listar_laboratorios()
            
            elif opcao == 3:
                atualizar_laboratorios()

            elif opcao == 4:
                excluir_laboratorios()

    except ValueError:
        print("Erro: digite apenas numeros!")

    finally:
        print("------------------------------------------------")



def menu_principal():
    try:
        opcao = 0

        while opcao != 3:
            print("----------------LABORATORIO DE EXAMES----------------")
            print("1-redes")
            print("2-laboratorios")
            print("3-sair")
            opcao = int(input("escolha uma das opcoes a cima:"))
            print("----------------------------------------------")

            if opcao == 1:
                menu_redes()

            elif opcao == 2:
                menu_laboratorios()

    except ValueError:
            print("Erro: digite apenas numeros!")

    finally:
        print("prograna encerrado!")
        print("--------------------------------------------------")

menu_principal()
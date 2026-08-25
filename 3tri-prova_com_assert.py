import sqlite3

def cadastrar_redes(nome_grupo, sac, banco):
    try: 
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS redes_diagnosticos(
                        id_rede INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_grupo TEXT NOT NULL,
                        sac TEXT NOT NULL
                        )''')

        comando_inserir = (f'''INSERT INTO redes_diagnosticos 
                            (nome_grupo , sac)
                            VALUES('{nome_grupo}', '{sac}')''')

        cursor.execute(comando_inserir)
        conexao.commit()
        return "rede de exames cadastrada!"

    except sqlite3.Error as erro:
        print("Erro no banco de dados!")

    finally:    
        conexao.close()



def listar_redes(banco):
    try:
        conexao = sqlite3.connect(banco)
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

        return "listado com sucesso!"
        
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    finally:
        conexao.close()



def atualizar_redes(id_rede , novo_nome_rede , novo_sac , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''
        UPDATE redes_diagnosticos
        SET nome_grupo = '{novo_nome_rede}',
            sac = '{novo_sac}'
        WHERE id_rede = {id_rede}
        '''

        cursor.execute(sql)

        conexao.commit()

        if cursor.rowcount > 0:
            print("rede atualizado com sucesso!")
        else:
            print("Nenhuma rede foi encontrada com esse ID!")

        return "rede atualizada!"

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados!")

    except ValueError:
        print("Erro: digite apenas numeros!") 

    finally:
        conexao.close()



def excluir_redes(id_rede , banco):
    try:
        conexao = sqlite3.connect(banco)
        cursor = conexao.cursor()

        sql = f'''DELETE FROM redes_diagnosticos WHERE id_rede = {id_rede}'''

        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount > 0:
            return "rede excluído com sucesso!"
        else:
            return "Nenhuma rede foi encontrada com esse ID."

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
                nome_grupo = input("digite o nome do grupo:")
                sac = input("digite o SAC:")
                banco = 'laboratirio_exames.db'
                cadastrar_redes(nome_grupo, sac, banco)

            elif opcao == 2:
                banco = 'laboratirio_exames.db'
                listar_redes(banco)
            
            elif opcao == 3:
                id_rede = int(input("Digite o ID da rede que deseja alterar: "))
                novo_nome_rede = input("digite o novo nome do grpo:")
                novo_sac = input("digite o novo SAC:")
                banco = 'laboratirio_exames.db'
                atualizar_redes(id_rede , novo_nome_rede , novo_sac , banco)

            elif opcao == 4:
                id_rede = int(input("Digite o ID da rede que deseja excluir: "))
                banco = 'laboratirio_exames.db'
                excluir_redes(id_rede , banco)

    except ValueError:
        print("Erro: digite apenas numeros!")
    finally:
        print("------------------------------------------------")


def cadastrar_laboratorios (endereco_laboratorio , id_rede , banco):
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
                endereco_laboratorio = input("digite o endereco do laboratorio:")
                id_rede = int(input("digite o ID da rede em que o laboratorio esta inserido:"))
                banco = 'laboratirio_exames.db'
                cadastrar_laboratorios(endereco_laboratorio , id_rede , banco)

            elif opcao == 2:
                banco = 'laboratirio_exames.db'
                listar_laboratorios(banco)
            
            elif opcao == 3:
                id_laboratorio= int(input("Digite o ID do laboratorio que deseja atualizar: "))
                novo_endereco = input("Digite o novo endereco: ")
                banco = 'laboratirio_exames.db'
                atualizar_laboratorios(id_laboratorio , novo_endereco , banco)

            elif opcao == 4:
                id_laboratorio = int(input("Digite o ID do laboratorio que deseja excluir: "))
                banco = 'laboratirio_exames.db'
                excluir_laboratorios(id_laboratorio , banco)

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
            print("--------------------------------------1-------")

            if opcao == 1:
                menu_redes()
            elif opcao == 2:
                menu_laboratorios()

    except ValueError:
            print("Erro: digite apenas numeros!")

    finally:
        print("prograna encerrado!")
        print("--------------------------------------------------")

# menu_principal()
 
#testes redes
assert cadastrar_redes("amora" , "sac", 'laboratirio_exames_teste.db') == "rede de exames cadastrada!"
assert listar_redes('laboratirio_exames_teste.db') == "listado com sucesso!"
assert atualizar_redes(1 , "abacate" , "sac" , 'laboratirio_exames_teste.db') == "rede atualizada!"
assert excluir_redes(7 , 'laboratirio_exames_teste.db') == "rede excluído com sucesso!"
# assert excluir_redes(10 , 'laboratirio_exames_teste.db') == "Nenhuma rede foi encontrada com esse ID."

#testes laboratorios
assert cadastrar_laboratorios("paranavai" , 6 , 'laboratirio_exames_teste.db') == "laboratorio cadastrado!"
assert listar_laboratorios('laboratirio_exames_teste.db') == "listado com sucesso!"
assert atualizar_redes(1 , "piracema" , 'laboratirio_exames_teste.db') == "laboratorio atualizada!"
assert excluir_laboratorios(1 , 'laboratirio_exames_teste.db') == "laboratorio excluído com sucesso!"
assert excluir_laboratorios(10 , 'laboratirio_exames_teste.db') == "Nenhum laboratorio foi encontrado com esse ID."
print("testes concluidos!")
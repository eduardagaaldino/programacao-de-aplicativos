import sqlite3

def cadastrar_escola_manual():
    # O aluno resolveu gerar o ID por conta própria
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash).
    # Aplique a blindagem protetora necessária:
    try:
    cursor.execute(
        "INSERT INTO escolas (id, nome) VALUES (?, ?)",
        (id_escola, nome)
    )

    conexao.commit()
    print("nova escola cadastrada!")

    except sqlite3.IntegrityError:
        print("Erro, já existe uma escola cadastrada com esse ID!")

    finally:
        conexao.close()

#devesse usar o try, except e finally
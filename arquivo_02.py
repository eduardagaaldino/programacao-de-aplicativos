print("----------bons habtos---------")

def criar_arquivo():
    open('habitos.txt' , 'w').close()

def inserir():
    habito = input("Coloque a seguir um novo hábito que deseja começar: ")
    with open('habitos.txt' , 'a') as h:
        h.write(habito + '\n')
        print("Hábito cadastrado com sucesso!")

def ler():
    with open('habitos.txt' , 'r') as h:
        habito = h.readlines() 

        i = 0
        for ha in habito:
            print(f"\n{i} - {ha.strip()}")
            i += 1

def ajustar():
    ler()
    indice = int(input("\nDigite o ID do hábito que deseja ajustar: "))
    novo_habito = input("Digite o novo hábito: ")

    with open('habitos.txt' , 'r') as h:
        linhas = h.readlines()

        linhas[indice] = novo_habito + '\n'

    with open('habitos.txt' , 'w') as h:
        h.writelines(linhas)
        print("Hábito atualizado com sucesso!")

def descartar():
    ler()
    ind = int(input("\nInforme o ID do hábito que deseja descartar: "))

    with open('habitos.txt' , 'r') as h:
        linhas = h.readlines()

    del linhas[ind]

    with open('habitos.txt' , 'w' ) as h:
        h.writelines(linhas)
        print("Hábitos removidos com sucesso!")

while True:
    print("\n---MURAL DE BONS HÁBITOS---")
    print("\n1- Adicionar novos hábitos")
    print("2-Listar hábitos")
    print("3-Editar hábitos")
    print("4-Excluir hábitos")
    print("5-Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1': inserir()
    elif opcao == '2': ler()
    elif opcao == '3': ajustar()
    elif opcao == '4': descartar()
    elif opcao == '5':
        print("Programa encerrado!")
        break
print("-"*35)
def menu():
    opcao == 0
    while opcao =! 2:
        print("1. Cadastrar Aluno")
        print("2. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa.")
            #Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 

#pq deveria ter uma varial opcao = 0 e no lugar do true deveria ser um opcao =! 2:
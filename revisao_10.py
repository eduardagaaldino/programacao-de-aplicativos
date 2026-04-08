print("-------")

usuario = ["joao", "maria", "livia", "nicolas"]
nomes = []

print("1 - Adicionar usuário")ydc,if

opcao = input("Escolha uma opção: ")

while opcao != "3": 
    if opcao == "1":
        nome= input("Digite o nome de usuário: ")
        senha = int(input("Digite a senha: "))

        #continuar

        if nome in usuario:
            print("Usuário já existe!")
        else:
            nomes[usuario] = senha
            print("Usuário cadastrado com sucesso!")

        opcao = input("Escolha uma opção: ")

    elif opcao == "2":
        usuario = input("Usuário: ")
        senha = int(input("Senha: "))

        if usuario in nomes  and nomes[usuario] == senha:
            print(f"Bem-vindo, {usuario}!")
        else:
            print("Usuário ou senha incorretos!")
        
        opcao = input("Escolha uma opção: ")

    elif opcao == "3":
        print("Saindo do sistema...")
    else:
        print("Opção inválida! Tente novamente.")

print("Saindo do sistema...")
print("--------------------------------")
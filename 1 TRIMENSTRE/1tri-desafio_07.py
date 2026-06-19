print("\n---------------desafio biblioteca---------------")

livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
print("\n---listas iniciais---")
print(f"livros disponoveis:{livros_disponiveis}")
print(f"livros emprestados:{livros_emprestados}")
nome_livro = input("\ndigite o nome do livro que deseja emprestar: ")

if nome_livro in livros_disponiveis:
    livros_emprestados.append(nome_livro)
    livros_disponiveis.remove(nome_livro)
    print("emprestimo realizado com sucesso!")

else:
    print("Este livro não consta como emprestado.")

nome_livro_emprestado = input("\ndigite o nome do livro que deseja devolver: ")

if nome_livro_emprestado in livros_emprestados:
        livros_disponiveis.append(nome_livro_emprestado)
        livros_emprestados.remove(nome_livro_emprestado)
        print("\ndevolucao realiada com sucesso!")

else:
    print("\nEste livro não consta como emprestado.")

del livros_disponiveis [0:1]

print("\n---listas finais---")
print(f"livros dispiniveis:{livros_disponiveis}")
print(f"livros emprestados:{livros_emprestados}")
print("\n---------------------------------------------------")
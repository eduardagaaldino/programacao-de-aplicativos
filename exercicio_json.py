#importa o arquivo
import json
#verifica se o arquivo ja existe
import os

#define a variavel "BANCO_DADOS" como um arquivo .json
BANCO_DADOS = 'alunos.json'

#funcao de adicionar um aluno
def cadastrar():
    #exibe "novo cadastro" no terminal
    print("\n--- Novo Cadastro ---")
    
    #se o arquivo existir
    if os.path.exists(BANCO_DADOS):
        #abra o arquivo no modo de leitura e  o salvacomo f
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            #le o arquino 
            alunos = json.load(f)
    #caso contrario
    else:
        #cria uma lista vazia chamada alunos
        alunos = []

    #cria uma variavel chamada "novo_aluno"que salva os dados do aluno 
    novo_aluno = {
        #pede o nome do aluno e o salva na variavel "nome"
        "nome": input("Nome: "),
        #pede o telefone do aluno e o salva na variavel "telefone"
        "telefone": input("Telefone: "),
        #pede a turma do aluno e o salva na variavel "turma"
        "turma": input("Turma: "),
        #pede a idade do aluno e o salva na variavel "idade"
        "idade": int(input("Idade: ")),
        #pede o cpf do aluno e o salva na variavel "cpf"
        "cpf": input("CPF: ")
    #fecha a variavel
    }
    
    #adiciona o aluno cadastrado na lista alunos
    alunos.append(novo_aluno)

    #abre o arquivo no modo leitura e o salve como f
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        #escreve no arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False)

    # exibe "Aluno cadastrado com sucesso!"  no terminal
    print("Aluno cadastrado com sucesso!")

#funcao de mostrar os alunos cadastrados
def listar():
    # exibe "lista de alunos" no terminal
    print("\n--- Lista de Alunos ---")
    
    #se o arquivo existir entao
    if os.path.exists(BANCO_DADOS):
        #abra o arquino 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            ##salva o arquivo em uma variavel chamada alunos
            alunos = json.load(f)
    #caso contrario 
    else:
        #cria uma lista vazia chamada alunos
        alunos = []

    #se os dados nao existirem entao 
    if not alunos:
        # exibe "Nenhum aluno cadastrado." no terminal
        print("Nenhum aluno cadastrado.")
        #encerra a funcao
        return

    #pra cada aluno da lista alunos
    for aluno in alunos:
        #exibe o nome, cpf, turma e telefone do aluno no terminal 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

#funcao de alterar os dados dos alunos cadastrados
def atualizar():
    # exibe " atualizar aluno " no terminal
    print("\n--- Atualizar Aluno ---")
    #se o arquivo nao existir entao 
    if not os.path.exists(BANCO_DADOS):
        #exibe "Nenhum aluno cadastrado no sistema." no terminal 
        print("Nenhum aluno cadastrado no sistema.")
        #encerra a funcao
        return

    #abre o arquivo no modo de leitura e o salva como f
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #le o arquino 
        alunos = json.load(f)
    #pede o cpf do aluno que deseja editar e o salva em uma variavel
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")
    
    #pra cada aluno da lista alunos
    for aluno in alunos:
        #se o cpf do aluno for igual a "cfp_busca"
        if aluno['cpf'] == cpf_busca:
            # exibe "Editando dados de:" + o nome do aluno no terminal
            print(f"Editando dados de: {aluno['nome']}")
            #atualiza o nome do aluno
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            #atualiza o telefone do aluno 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            #atualiza a turma do aluno
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            #atualiza a idade do aluno 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            #atualiza o cpf do aluno
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            #abre o arquivo no modo de escrever/sobreescrever e o salve como f
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                #escreve no arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            # exibe "Dados atualizados com sucesso!" no terminal  
            print("Dados atualizados com sucesso!")
            #encerra a funcao
            return
            
    # exibe "Aluno não encontrado." no terminal 
    print("Aluno não encontrado.")

#funcao de excluir o cadastro de um aluno
def excluir():
    # exibe "excluir aluno" no terminal
    print("\n--- Excluir Aluno ---")
    #se o arquivo nao existir entao 
    if not os.path.exists(BANCO_DADOS):
        # exibe "Nenhum aluno cadastrado no sistema." no terminal 
        print("Nenhum aluno cadastrado no sistema.")
        #encerra a funcao
        return

    #abre o arquino no modo de leitura e o salve como f 
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #le o arquivi 
        alunos = json.load(f)
    #pede o cpf do aluno que deseja remover e o salva em variavel    
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    #remove um aluno da lista pelo cfp
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    #se a nova_lista for menor do que alunos entao: 
    if len(nova_lista) < len(alunos):
        #abre o arquino no medo de escrever/sobreescrever e o salve como f
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            #escreve no arquivo 
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        #exibe "Aluno removido com sucesso!" no terminal 
        print("Aluno removido com sucesso!")
    #caso contrario
    else:
        #exibe "Aluno não encontrado."
        print("Aluno não encontrado.")

#funcao que montra o menu
def menu():
    #se o arquivo nao existir entao 
    if not os.path.exists(BANCO_DADOS):
        #abre o arquivo no modo de escrever/sobreescrever e o salve como f
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            #eescreve no arquivo
            json.dump([], f)

    #enquanto for verdade
    while True:
        #exibe "sistema escolar" no terminal
        print("\n=== SISTEMA ESCOLAR ===")
        #exibe "1. Cadastrar Aluno" no terminal
        print("1. Cadastrar Aluno")
        #exibe "2. Listar Alunos" no terminal
        print("2. Listar Alunos")
        #exibe "3. Atualizar Aluno" no terminal 
        print("3. Atualizar Aluno")
        #exibe "4. Excluir Aluno" no terminal
        print("4. Excluir Aluno")
        #exibe "5. sair" no terminal
        print("5. Sair")
        #pede a que escolham umas das opcoes do menu e salva em uma variavel
        opcao = input("Escolha uma opção: ")
        
        #se opcao for igual a 1 entao faca a funcao de cadastrar aluno
        if opcao == '1': cadastrar()
        #se opcao for igual a 2 entao faca a funcao de listar alunos
        elif opcao == '2': listar()
        #se opcao for igual a 3 entao faca a funcao de atualizar aluno
        elif opcao == '3': atualizar()
        #se opcao for igual a 4 entao faca a funcao de excuir aluno
        elif opcao == '4': excluir()
        #se opcao for igual a 5 entao encerre o programa
        elif opcao == '5': break
        #caso contrario exiba "opcao invalida" no terminal
        else: print("Opção inválida!")

#chama a funcao de menu
menu()
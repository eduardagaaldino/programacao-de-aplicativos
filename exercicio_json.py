print("----------escola digital----------")

import json

def cadatrar():
    nome = input("digite seu nome: ")
    cpf = input("digite seu cpf: ")
    telefone = input("digite se telefone: ")
    turma = input("digite sua turma: ")
    idade = input("digite sua idade: ")

    aluno = {
        "nome" : nome,
        "cpf" : cpf,
        "telefone" : telefone,
        "turma" : turma,
        "idade" : idade
    }

opcao = 0
while opcao != 5:
    print("----------menu----------")
    print("1- cadatrar aluno")
    print("2- listar alunos")
    print("3- atualizar dados")
    print("4- remover aluno")
    print("5- sair")
    opcao = int(input("escolha uma das opcoes acima: "))
    print("------------------------")

    if opcao == 1:
        cadatrar()

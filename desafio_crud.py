print("-------desafio funcao--------")

def adicionar_produto(nome,lista):
    lista.append(nome)

def listar_produtos(lista):
    for l in lista:
        indice = lista.index(l)
        print(f"o indice do produto {l} é: {indice}")

def atualizar_produto(nome,novo_nome,lista):
    indice = lista.index(nome)
    lista[indice]=novo_nome

def remover_item(nome,lista):
    lista.remove(nome)

def exibir_menu(menu):
    while menu != 6:
        print("\n-------------------------------------------")
        print("<<<< MENU INICIAL >>>>")
        print("1-adicionar produto")
        print("2-listar produto")
        print("3-atualizar produto")
        print("4-remover produto")
        print("5- estoque atual")
        print("6-sair")
        print("---------------------------------------------")
        menu = int(input("escolha uma das opcoes a cima: "))
       
        if menu == 1:
            produto = input("digite o produto que vc deseja adicionar ao estoque: ")
            adicionar_produto(produto,estoque)

        elif menu == 2:
            listar_produtos(estoque)

        elif menu == 3:
            removido = input("digite o produto que vc deseja trocar do estoque: ")
            novo_produto = input("digite o produto que vc deseja adicionar no lugar:")
            atualizar_produto(removido,novo_produto,estoque)

        elif menu == 4:
            produto = input("digite o produto que voce deseja remover: ")
            remover_item(produto,estoque)

        elif menu == 5:
            print("estoque atual: " , estoque)

        elif menu == 6:
            print("estoque final: ", estoque)
            print("programa finalizado!")        

estoque = []
menu = 0
exibir_menu(menu)

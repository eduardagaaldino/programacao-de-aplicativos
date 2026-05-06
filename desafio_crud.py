print("-------desafio funcao--------")

def adicionar_produto(nome,lista):
    lista.append(nome)
    print("estoque atual: " , lista)

def listar_produtos(lista):
    for l in lista:
        indice = lista.index(l)
        print("indice: " , indice)

def atualizar_produto(nome,indice,lista):
    lista[indice]=nome

def remover_item(indice,lista):

    lista.remove(indice)

def exibir_menu(menu):
    while menu != 5:
        print("\n-------------------------------------------")
        print("<<<< MENU INICIAL >>>>")
        print("1-adicionar produto")
        print("2-listar produto")
        print("3-atualizar produto")
        print("4-remover produto")
        print("5-sair")
        menu = int(input("escolha uma das opcoes a cima: "))
       
        if menu == 1:
            produto = input("digite o produto que vc deseja adicionar ao estoque: ")
            adicionar_produto(produto,estoque)

            



estoque = []
menu = 0
exibir_menu(menu)
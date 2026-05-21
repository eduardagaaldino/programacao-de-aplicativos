print("------------viagem------------")

def criar_arquivo():
    open("viagem.txt" , 'w').close()


def adicionar_destinos():
    destino = input("digite sua sugestao de destino: ")
    with open("viagem.txt" , 'a') as arquivo:
        arquivo.write(destino + "\n")
    print(f"o destino {destino} foi adicionado!")

def ler_destinos():
    with open("viagem.txt" , 'r') as arquivo:
        destinos = arquivo.readlines()
        
        posicao = 0
        for d in destinos:
            print(f"{d.strip()}({posicao})")
            posicao += 1

def atualizar_destino():
    ler_destinos()
    alterar = int(input("digite o id do destino que vc deseja alterar: "))
    novo = input("digite o novo destino: ")

    with open("viagem.txt" , 'r') as arquivo:
        destinos = arquivo.readlines()

    destinos[alterar] = novo + "\n"

    with open("viagem.txt" , 'w') as arquivo:
        arquivo.writelines(destinos)
    print("destino atualizado!")

def deletar_destino():
    ler_destinos()
    deletar = int(input("digite o id do destino que vc deseja deletar: "))
    
    with open("viagem.txt" , 'r') as arquivo:
        destinos = arquivo.readlines()

    del destinos[deletar] 

    with open("viagem.txt" , 'w') as arquivo:
        arquivo.writelines(destinos)
    print("destino removido!") 



opcao = 0

while opcao != 5:
    print(25 * "-")
    print("1- adicionar destino")
    print("2- listar destinos")
    print("3- alterar destino")
    print("4- remover destino")
    print("5- sair")
    print(25 * "-")
    opcao = int(input("escolha uma das opcoes a cima: "))

    if opcao == 1:
        adicionar_destinos()

    elif opcao == 2:
        ler_destinos()
    
    elif opcao == 3:
        atualizar_destino()

    elif opcao == 4:
        deletar_destino()
print("programa encerrao!")
print("------------------------------")
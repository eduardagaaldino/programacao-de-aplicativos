def criar_arquivo():
    open("viagem.txt" , 'w').close()


def adicionar_destinos():
    destino = input("digite sua sugestao de destino: ")
    with open("viagem.txt" , 'a') as arquivo:
        arquivo.write(destino + "\n")
    print(f"o destino {destino} foi adicionado!")


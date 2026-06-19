print("----------busca de nomes----------")

nomes = ["ana", "weldel", "joao", "gustavo", "pedro", "camila"]
verificar = input("digite seu nome de verificaçao: ")

if verificar in nomes:
    print(f"O nome {verificar} está na lista!")
else:
    print(f"O nome {verificar} não foi encontrado na lista.")

print("-------------------------------------")
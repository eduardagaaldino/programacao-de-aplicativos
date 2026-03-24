print("\n---------Localizador Inteligente----------")

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]

print(f"\nsta antiga: {cidades}")

nome_cidade = input("digite o nome da sua cidade: ")

if nome_cidade in cidades:
    cidades.index(nome_cidade)
    print(f"\nA cidade {cidades} está na posicao {nome_cidade}.")

else:
    print("\ninformacao invalida!")

print(f"\nlista atual: {cidades}")
print("\n---------Localizador Inteligente----------")

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]

print(f"\nsta antiga: {cidades}")

nome_cidade = input("\ndigite o nome da sua cidade: ")

if nome_cidade in cidades:
    posicao = cidades.index(nome_cidade)
    print(f"\nA cidade {nome_cidade} está na posicao {posicao}.")

else:
    print("\ninformacao invalida!")

print(f"\nlista atual: {cidades}")
print("---------------------------------------------")
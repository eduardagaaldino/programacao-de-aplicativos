print("\n----------Entrada de Dados---------")

carrinho = []
produto = ""

while produto != "fim":
    produto = input("\ndigite o produto desejado: ")
    if produto != "fim":
        carrinho.append(produto)
        print(f"{produto} foi adicionado a o carinho!")

print(f"\ncarinho atual: {carrinho}")
print("\n-------------------------------------")
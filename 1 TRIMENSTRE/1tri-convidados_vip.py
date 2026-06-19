print("----------Apenas nomes com A são permitidos no VIP----------")

lista_vip = []
nome =""

while nome != "fim":
    nome = input("\ndigite o nome do convidado:")

    if nome != "fim":
        if nome[0] == "a":
            lista_vip.append(nome)

            print(nome ,"foi adicionado a lista VIP!")

        else:
            print("Apenas nomes com A são permitidos no VIP!")


print(f"\nlista VIP: {lista_vip}")
print("------------------------------------------------------------")
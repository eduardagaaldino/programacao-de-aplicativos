print("---------- O Somador de Carrinho ----------")

def somar_carrinho(precos):
    total = 0
    for p in precos:
        total += p

    if total > 500.00:
        desconto = total * 0.10
        total -= desconto

    return total

lista = [20,89,90,65,87,32,67,44,77,90,21]

valor_final = somar_carrinho(lista)
print(f"o valor total da compra foi: {valor_final}")
print("--------------------------------------------")
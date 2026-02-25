valor = float(input("digite o valor total da compra:"))
cupom = input("digite o codigo do cupom")


if cupom == "DEV10":
    desconto = valor * 0.10
    valorD = valor - desconto
    print("valor com desconto:" , valorD)
else:
    print("cupom invalido, tente novamente.")
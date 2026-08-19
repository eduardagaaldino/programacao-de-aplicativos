def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

#sem desconto
assert calcular_desconto(100, 0) == 100

#10% de desconto
assert calcular_desconto(100, 10) == 90

#50% de desconto
assert calcular_desconto(200, 50) == 100

#100% de desconto
assert calcular_desconto(150, 100) == 0

#preço decimal
assert calcular_desconto(99.90, 10) == 89.91
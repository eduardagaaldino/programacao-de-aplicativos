# def calcular_desconto(preco, percentual):
#     return preco - percentual

# assert calcular_desconto(200, 0.1) == 180

def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

assert calcular_desconto(100, 0.1) == 90
assert calcular_desconto(200, 0.1) == 180
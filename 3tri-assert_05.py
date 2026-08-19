def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20

#abaixo de R$ 100
assert calcular_frete(80) == 20

#exatamente de R$ 100
assert calcular_frete(100) == 10

#entre R$ 100 e R$ 199,99
assert calcular_frete(150) == 10

#exatamente de R$ 200
assert calcular_frete(200) == 0

#acima de R$ 200
assert calcular_frete(250) == 0
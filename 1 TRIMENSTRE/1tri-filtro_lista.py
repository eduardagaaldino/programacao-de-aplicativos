print("\n----------Filtro de Lista----------")

nomes = ["ana" , "joana" , "carlos" , "pablo" , "ester" , "camila" , "ema"]
print(f"\nlista antiga: {nomes}")

for nome in nomes:
    if len(nome) >= 5:
        print(f"\nlista atual: {nome}")

print("\n------------------------------------")
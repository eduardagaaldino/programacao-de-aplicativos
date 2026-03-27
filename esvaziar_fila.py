print("----------Esvaziando a Fila----------")

nomes = ["ema" , "eduarda" , "jaferson" , "manuelly", "guilherme"]
print(f"\nlista antiga{nomes}")

while nomes:
    nome = nomes.pop(0)
    print(f"\n{nome}, foi atendido!")

print("\ntodos os clientes foram atendidos!")
print("\n-----------------------------------")
idade = int(input("digite sua idade: "))
ingresso = input("possui ingresso? (s/n): ")
lista = input("esta na lista? (s/n): ")

if idade >= 18 and (ingresso == "s" or lista == "s"):
    print("acesso liberado, aproveite o show!")

else:
    print("acesso negado!")
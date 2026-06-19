codigo = int(input("\n digite o codigo do pacote: "))
peso = int(input("digite o peso do pacote: "))

if peso < 5 and codigo %10 == 0:
    print(f"pacote {codigo}: entrega expressa!")

elif peso > 50 and codigo %10 == 0:
    print(f"pacote {codigo}: carga pesada!")

else:
    print(f"pacote {codigo}: carga nao autorizada!")
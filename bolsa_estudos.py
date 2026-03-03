medida =  float(input("digite sua media: "))
renda = float(input("digite sua renda familar : "))
estudante_de_publica = input("veio de escola publica? (s/n): ")

if medida >= 8.0 and (renda <= 2000.00 or estudante_de_publica == "s"): 
    print("parabens! voce ganhou uma bolsa de estudos.")

else:
    print("voce nao atende os requisitos para a bolsa.")
    
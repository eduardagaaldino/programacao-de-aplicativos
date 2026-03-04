cargo = input("digite seu cargo: ")
codigo = int(input("digite seu codigo de acesso: "))
botao = input("o botao de emergencia esta precionado? (s/n): ")
epi = input("voce esta utilizando o epi completo: (s/n): ")

if cargo == "engenheiro" or "tecnico" and (codigo == 1234 or botao == "s") and (epi == "s"):
    print("acesso liberado! ")

else:
    print("acesso negado! ")
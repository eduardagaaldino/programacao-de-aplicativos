print("")
print("---seguranca no chao de fabrica---")
print("")

curso = input("voce concluiu o curso de seguranca? (s/n): ")

if curso == "s":
    instrutor = input("o instrutor esta presente na sala? (s/n): ")
    
    print("")

    if instrutor == "s":
        print("Acesso Liberado: Operação iniciada")

    else:
        print("Aguarde o instrutor para ligar a máquina")

else:
    print("Acesso Negado: Faça o treinamento primeiro")

print("")
print("-" * 35)
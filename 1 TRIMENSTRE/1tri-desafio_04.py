
numero = int(input("\n qual o numero da garrafa que esta passando pela esteira?: "))

if numero == 500:
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")
    print("QUALIDADE: Retirar amostra para teste.")

elif numero %500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")

elif numero %100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")

else:
    print(f"Produção em dia. Garrafa número {numero} processada.")
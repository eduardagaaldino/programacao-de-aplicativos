senha_acesso = (input("\n digite sua senha: "))
tentativa = int(input("digite o numero de tentativas: "))
token = input("possui token? (s/n): ")

senha = "admin123"

if senha_acesso == senha and tentativa %3 == 0 or token == "s":
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO.")

else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")
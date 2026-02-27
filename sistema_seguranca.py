nome = input("digite seu nome de usuario: ")
codigo = int(input("digite o codigo secreto: "))


if nome == "admin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online.")
else:
    print("Falha na autenticação. Alerta de segurança ligado!")
usuario = input("digite o seu usuario: ")
senha = int(input("digite sua senha de acesso: "))

if (usuario == "admin" or usuario == "root") and senha == 12345:
    print("acesso liberado!")

else:
    print("acesso negado!")
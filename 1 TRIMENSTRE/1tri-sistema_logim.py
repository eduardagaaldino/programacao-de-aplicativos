print("\n------------Sistema de Login------------")

senha_correta = 12345

senha = int(input("digite sua senha: "))

while senha != senha_correta:
    senha = int(input("senha incorreta, tente novamente: "))

print("\nbem vindo!")
print("\n-----------------------------------------")
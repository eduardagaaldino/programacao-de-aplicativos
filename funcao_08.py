print("----------Analisador de Texto----------")

def contar_caracteres(palavra):
    tamanho = len(palavra)
    return tamanho

nome = input("digite um nome:")

tamanho = contar_caracteres(nome)

if tamanho < 5:
    print("Nome de usuário muito curto!")

else:
    print("Nome aceito!")

print("---------------------------------------")
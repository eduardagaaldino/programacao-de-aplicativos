print("\n----------Limpeza de Cadastro (del vs remove)----------")

usuarios = ["admin", "convidado", "suporte", "teste"]
print(f"\nlista antiga:{usuarios}")

usuarios.remove("teste")
del usuarios [0]

print(f"\nlista final:{usuarios}")
print("\n--------------------------------------------------------")
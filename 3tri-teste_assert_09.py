def buscar_nome(lista, nome):
    return nome in lista

def tem_senha_valida(senha):
    return len(senha) >= 8

assert buscar_nome(["Ana", "João", "Maria"], "Ana") == True
assert buscar_nome(["Ana", "João", "Maria"], "Pedro") == False
#assert buscar_nome([], "Ana") == True

assert tem_senha_valida("1234567") == False
assert tem_senha_valida("12345678") == True
#assert tem_senha_valida("senha123") == False
def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

#maior de idade desacompanhada
assert pode_entrar(20, False) == True

#menor de idade acompanhada
assert pode_entrar(16, True) == True

#menor de idade desacompanhada
assert pode_entrar(16, False) == False

#exatamente 18 anos
assert pode_entrar(18, False) == True

#17 anos acompanhada
assert pode_entrar(17, True) == True
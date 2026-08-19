def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

#acima de 6
assert situacao_aluno(8) == "Aprovado"

#exatamente igual a 6
assert situacao_aluno(6) == "Aprovado"

#exatamente igual a 4
assert situacao_aluno(4) == "Recuperação"

#abaixo de 4
assert situacao_aluno(3) == "Reprovado"

#numero decimal
assert situacao_aluno(5.9) == "Recuperação"
print("---------filtro de aprovados----------")

alunos = ["joao", "maria", "lana", "lucas", "luis"]
notas = [80, 70, 100, 99, 55]

for nota in notas:
    if nota >= 60:
        indice = notas.index(nota)
        print(alunos[indice])

print(f"aprovados: {alunos}")
print("---------------------------------------")

#corrigir/entender
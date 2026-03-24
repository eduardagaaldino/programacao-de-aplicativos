print("----------Transferência de Arquivos----------")

pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluidos = []

print("\nlistas antigas")
print(f"1- {pendentes}")
print(f"2-{concluidos}")

concluidos.append(pendentes[0])
pendentes.pop(0)

print("\nlistas atuais:")
print(f"1-{pendentes}")
print(f"1-{concluidos}")
print("\n -----------------------------------------------")
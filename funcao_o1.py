print("---------classificador de notas--------")

def avaliar_desempenho (nota):
    if nota >= 9:
        print("exelente")

    elif nota >= 7:
        print("bom")

    elif nota > 5:
        print("regular")

    else:
        print("insuficiente")

nota = float(input("digite sua nota: "))

avaliar_desempenho(nota)
print("---------------------------------------")
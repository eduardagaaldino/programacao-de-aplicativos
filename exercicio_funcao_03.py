print("----------aplicador de desconto-----------")

def aplicar_promocao(precos):
    lista = []

    for p in precos:
        if p > 100:
            desconto = p * 0.15
            preco_final = p - desconto
            lista.append(p)

        else: 
            lista.apend(p) 

    return lista

lista = []
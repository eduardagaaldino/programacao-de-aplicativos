print("----------aplicador de desconto-----------")

def aplicar_promocao(precos , lista):

    for x in precos:
        if x > 100.0:
            desconto = x * 0.15
            preco_final = x - desconto
            lista.append(preco_final)

        else: 
            lista.append(x) 

    return lista

lista = [150.0, 80.0, 200.0, 50.0]
nova_lista = []

lista_atual = aplicar_promocao(lista , nova_lista)

print("lista antiga: " , lista)
print("lista atualizada: " , lista_atual)
print("-------------------------------------------")
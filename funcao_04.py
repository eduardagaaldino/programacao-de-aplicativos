print("----------localizador de itens----------")

def esta_na_lista(lista , buscar):

    for x in lista:
        if x == buscar:
            return "Encontrado!"

        else:
            return "Não disponível"

frutas = ["uva" , "maca" , "pera" , "banana" , "kiui" , "morango"]
buscar = input("qual fruta vc procura?: ")

fruta_desejada = esta_na_lista(frutas , buscar)
print(fruta_desejada)
print("----------------------------------------")
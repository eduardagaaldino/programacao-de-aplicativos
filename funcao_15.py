print("-----------Formatador de Endereços Nacionalizado------------")

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"\nRUA:{rua}, NUMERO:{numero}, BAIRRO:{bairro}, CIDADE:{cidade}, CEP:{cep}"

print("digite o endereco do destinatario:")
rua = input("rua:")
numero = input("numero:")
bairro = input("bairro:")
cidade = input("cidade:")
cep = int(input("cep:"))

etiqueta = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print(etiqueta)
print("------------------------------------------------------------")
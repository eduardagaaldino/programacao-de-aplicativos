print("----------Sistema de Checkout com Imposto e Desconto----------")

def calcular_preco_final(valor, imposto, cupom):
    if cupom > valor:
        return  0
    valor += imposto
    valor -= cupom
    return valor

valor_base = int(input("\nDigite o valor base: "))
imposto_percentual = int(input("Digite o valor do imposto: "))
cupom_desconto = int(input("Digite o valor do cupom: "))

resultado = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)
print(resultado)
print("------------------------------------------------------------------")
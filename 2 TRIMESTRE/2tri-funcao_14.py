print("----------Filtro Avançado de Candidatos (RH)----------")

def verificar_aprovacao(nota,ano,certificado):
    if nota >= 80 and ano >= 2 or certificado == "s":
        return "canditado aprovado, contrada!"

    else:
        return "candidata descartada!"


nota_teste = float(input("digite a nota que vc tirou no teste: "))
anos_xp = int(input("digite quantos anos vc tem de experiencia: "))
certificacao = input("possiu certificacao? (s/n): ")

resultado = verificar_aprovacao(nota_teste,anos_xp,certificacao)
print(resultado)
print("-------------------------------------------------------")
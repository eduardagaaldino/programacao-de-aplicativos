print("----------Verificador de Paridade----------")

def eh_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número: "))

par_impar = eh_par(numero)
print("Seu número é", par_impar)
print("-------------------------------------------")
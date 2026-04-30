print("----------Calculadora de Área de Terrenos----------")

def calcular_area(largura , comprimento, vezes):
    while vezes != 3:
        area = largura * comprimento
        print(f"a area e de: {area} metros")

        largura = float(input("digite a largura em metros: "))
        comprimento = float(input("digite o comprimento em metros: "))
        vezes += 1

print("----------------------------------------------------")

largura = ""
comprimento = ""
vezes = 0
area = calcular_area(largura , comprimento)
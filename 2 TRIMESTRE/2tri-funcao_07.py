print("----------Calculadora de Área de Terrenos----------")

def calcular_area(largura , comprimento, vezes):
    while vezes != 3:
        largura = float(input("digite a largura em metros: "))
        comprimento = float(input("digite o comprimento em metros: "))
        area = largura * comprimento
        print(f"a area e de: {area} metros")
        vezes += 1

largura = ""
comprimento = ""
vezes = 0
calcular_area(largura , comprimento , vezes)
print("----------------------------------------------------")
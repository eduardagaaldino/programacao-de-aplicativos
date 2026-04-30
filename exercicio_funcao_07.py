print("----------Calculadora de Área de Terrenos----------")

def calcular_area(largura , comprimento):
    area = largura * comprimento
    return area

largura = ""
comprimento = ""
vezes = 0

while vezes != 3:
    largura = float(input("digite a largura em metros: "))
    comprimento = float(input("digite o comprimento em metros: "))
    area = calcular_area(largura , comprimento)
    print(f"a area e de: {area} metros")
    comprimento += 1

print("----------------------------------------------------")
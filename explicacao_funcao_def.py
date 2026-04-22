
#explicacao 
def calcular_valor_total(v1, v2, v3):
    total = v1+v2+v3
    return total #salva o valor para ser usado no codigo 

v1 = float(input("digite o valor 1: "))
v2 = float(input("digite o valor 2: "))
v3 = float(input("digite o valor 3: "))

valor_total = calcular_valor_total(v1, v2, v3) #agora o valor_total vale o resultado 
print("o valor to tal e: " , valor_total)
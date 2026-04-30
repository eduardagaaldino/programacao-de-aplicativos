print("--------- O Conversor de Velocidade ----------")

def converter_km_para_ms(km_h):
    m_s = km_h / 3.6
    return m_s

velocidade = float(input("digite a velocodade em km/h: "))

if velocidade > 80.0:
    m_s = converter_km_para_ms(velocidade)
    print(f"voce esta a {m_s}m/s")
    print("reduza a velocidade!")

else:
    print("voce esta dentro do limite de velocidade permitido!")

print("------------------------------------------------")
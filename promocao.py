valor = float(input("digite o valor da compra: "))
prime = input("voce e cliente prime? (s/n): ")

frete = 50

if valor >= 500.00 or (prime == "s" and valor >= 100.00):
    frete = 0
    print("parbens! voce ganho frete gratis.")


valor_final = valor + frete


print("o valor final d sua compra sera de: " , valor_final)
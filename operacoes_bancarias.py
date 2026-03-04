
saldo = 1000.00

print("-" * 20)
print("menu inicial:")
print("1- deposito")
print("2- saque")
print("3- extrato")
print("-" * 20)

escolha = input(" escolha entre 1, 2 ou 3: ")

if escolha == "1":
    
    valor = float(input("digite o valor desejado : "))

    if valor > 0:

        valor_total = saldo + valor
        print("o valor total que a em sua conta e de: R$" , valor_total)

    else:
        print("deposito invalido!")

if escolha == "2":
    valor = float(input("digite o valor desejado : "))

    if valor > 0 and (valor <= saldo or valor == 100.00):

        valor_total = saldo - valor
        print("o valor total que a em sua conta e de: R$" , valor_total)

    else:
        print("saque invalido!")        

if escolha == "3":
   valor_total = saldo + 0
   print("o extrato da sua conta e de: R$" , valor_total)


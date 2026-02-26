idade = int(input("digite a sua idade: "))
saldo = float(input("digite seu saldo: "))

if idade >= 18 and saldo >= 50.00:
    print("Acesso autorizado! Bem-vindo ao evento")
elif idade < 18 and saldo < 50.00:
    print("Infelizmente voce nao cumpre os requisitos de entrada")
elif idade < 18 and saldo >= 50.00:
    print("Acesso negado!")
elif idade >= 18 and saldo < 50.00:   
    print("Acesso negado!")
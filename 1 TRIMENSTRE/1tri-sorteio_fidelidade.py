id = int(input("digite seu id: "))
valor = float(input("digite o valor da sua compra: "))

if id %2 == 0 and valor >= 500.00:
    print(f"Parabéns!, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor}")
    
else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")
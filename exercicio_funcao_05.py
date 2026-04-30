print("----------simulador de batalha RPG----------")

def sofrer_dano(dano , vida):

    while vida > 0:
        if dano > vida:
            return"game over!"
        
        if vida > 0: 
            vida -= dano
            print("vida atual: " , vida)
            dano = int(input("digite o dano que vc tomou: "))

    return "game over!"

vida = 100
dano = int(input("digite o dano que vc tomou: "))

final = sofrer_dano(dano , vida)
print(final)
print("--------------------------------------------")
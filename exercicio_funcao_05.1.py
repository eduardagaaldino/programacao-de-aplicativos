def sofrer_dano (valor_dano , vida_personagem):

    while vida_personagem > 0:
        if vida_personagem > 0:
            vida_personagem -= valor_dano
            print("vida atual: " , vida_personagem)

            valor_dano = int(input("digite o dano: "))

    return "game over!"

vida = 100
dano = int(input("digite o dano: "))

final = sofrer_dano(dano , vida)
print(final)
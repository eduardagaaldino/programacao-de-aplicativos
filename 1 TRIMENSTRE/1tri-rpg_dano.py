ataque = int(input("digite seu ataque:"))
defesa = int(input("digite sua defesa:"))


dano = ataque - defesa

if dano <= 0:
    print("o vilao bloqueo o ataque! dano;0")
elif dano > 0:
    print("Ataque critico! Voce causou dano ao vilao de:" , dano)
    
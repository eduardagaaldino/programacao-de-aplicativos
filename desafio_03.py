print("")
print("--sistema de poso dedrones de carga--")
print("")

codigo = int(input("digite o codigo do drone: "))
autorizacao = input("o drone possui autorizacao da torre? (s/n): ")

if codigo == 999 or autorizacao == "s":
    bateria = int(input("qual o nivel da bateria? (0 a 100): "))
    clima = input("como esta o clima? (ensolardo/chuvoso): ")
    vento = int(input("qual a velocidade do vento? (km/h): "))

#regra 01
    if bateria < 10:
        print("")
        print("pouso autorizado imediatamente por seguranca!")

#regra 02
    elif bateria >= 10 and (clima == "esolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
        print("")
        print("POUSO AUTORIZADO: Iniciando descida.")

    else:
        print("")
        print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")

else:
    print("")
    print("ERRO 01: Drone não identificado. Retornando à base.")

print("")
print("-" * 40)
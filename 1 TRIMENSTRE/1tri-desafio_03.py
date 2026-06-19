print("\n --sistema de poso dedrones de carga--")

codigo = int(input("\n digite o codigo do drone: "))
autorizacao = input("o drone possui autorizacao da torre? (s/n): ")

if codigo == 999 or autorizacao == "s":
    bateria = int(input("qual o nivel da bateria? (0 a 100): "))
    clima = input("como esta o clima? (ensolardo/chuvoso): ")
    vento = int(input("qual a velocidade do vento? (km/h): "))

#regra 01
    if bateria < 10:
        print("\n pouso autorizado imediatamente por seguranca!")

#regra 02
    elif bateria >= 10 and (clima == "esolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
        print("\n POUSO AUTORIZADO: Iniciando descida.")

    else:
        print("\n POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")

else:
    print("\n ERRO 01: Drone não identificado. Retornando à base.")

print("\n -" * 40)
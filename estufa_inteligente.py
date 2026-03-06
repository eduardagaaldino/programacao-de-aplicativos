print("")
print("---estufa inteligente---")
print("")

temperatura = float(input("qual a temperatura atual?: "))

if temperatura <= 30:
    print("Clima estável")

elif temperatura > 30:
    print("Alerta de Calor!")

    print("")

    umidade = float(input("qual a umidade atual?: "))
        
    if umidade < 40:
        print("Ação: Ligar Irrigação!")
     
    else:
        print("Ação: Ligar apenas ventiladores")

print("")
print("-" * 26)
print("\n-----Sensor de Temperatura com Alerta (Monitoramento)-----")

temperatura = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]

for t in temperatura:
    if t > 30.0:
        print(f"\n: Temperatura Crítica! ({t}°C)")

    else:
        print(f"\nTemperatura Normal. ({t}°C)")

controle = input("\ndeseja adicionar uma nova temperatura? (s/n): ")
add = float(input("\nnova temperatura: "))

while controle != "n":
    controle = input("\ndeseja adicionar uma nova temperatura? (s/n): ")

    if controle != "n":
        add = float(input("\nnova temperatura: "))
        temperatura.append(add)

print(f"\nlista atual: {temperatura}")
print("\n--------------------------------------------------------------------")
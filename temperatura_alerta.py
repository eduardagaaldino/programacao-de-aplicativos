print("\n-----Sensor de Temperatura com Alerta (Monitoramento)-----")

temperatura = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]

for t in temperatura:
    if t > 30.0:
        print(f"ALERTA: Temperatura Crítica! ({t}°C)")

    else:
        print(f"Temperatura Normal. ({t}°C)")

add = input("deseja adicionar uma nova temperatura? (s/n): ")

while add != "n":
    
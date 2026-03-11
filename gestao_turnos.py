id = int(input("/n digite seu id: "))
temperatura = float(input("digite a temperatura: "))
tempo = int(input("digite a tempo de uso: "))

if id %3 == 0 and temperatura > 40 and tempo > 8:
    print(f"Funcionário {id}, você foi escalado para a manutenção preventiva hoje.")

else:
    print(f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")
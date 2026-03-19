print("----------Verificador de Vagas----------")

vagas = ["Livre",  "Ocupado", "Livre", "Ocupado", ]
usuario = int(input("\n digite um numero de 0 a 3 que idica a sua vaga: "))

if usuario %2 == 0 and vagas[usuario] == "livre":
    print(f"Vaga {usuario} autorizada para estacionar.")

else:
    print( f"Vaga {usuario} indisponível ou fora das regras.")

print("\n -----------------------------------------")
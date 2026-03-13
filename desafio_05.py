print("-"* 40)
print("preencha com seus dados: ")

nome = (input("digite seu nome: ")) 
idade = int(input("digite sua idade: "))
telefone = int(input("digite seu numeero de telefone: "))
carteira = input("possui carteira de motorista? (s/n): ")

if nome == "joao" or nome == "thiago" or nome == "pedro" or nome == "matheus":
    print("")

if telefone == 99999999:
    print("Telefone Inválido")

if idade < 0 anda idade > 20:
    print("Idade inválida")

print(f"Olá {nome}, descobrimos que tem {idade}, rackeamos seu telefone {telefone} e será que você tem carteira? {carteira_de_motorista}". )
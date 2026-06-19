print("\n----------O Separador de Números (Lógica e Filtragem)----------")

numeros =[1,9,67,45,90,28,89,41,6,73,88]
pares = []
impares = []

print(f"\nlista inicial: {numeros}")

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

print(f"numeros pares: {pares}")
print(f"numeros impares: {impares}")
print("\n---------------------------------------------------------------")
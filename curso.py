nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
nota3 = float(input("digite sua nota: "))
presenca = int(input("digite sua presenca: "))

media = nota1 + nota2 + nota3

if media >= 70 and presenca >= 75:
    print("parabens! voce esta aprovado")
elif media < 70 and presenca < 75:
    print("Vice foi reprovado!")
elif media < 70 and presenca > 75:
    print("Vice foi reprovado!")
elif media > 70 and presenca < 75:
    print("Vice foi reprovado!")
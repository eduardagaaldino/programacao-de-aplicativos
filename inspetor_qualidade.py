print("")
print("-----sistema de qualidade-----")
print("")

comprimento = input("o comprimento da peca esta entre 10cm a 12cm? s/n: ")


if comprimento == "s":
    largura = input("a largura da peca esta entre 5cm a 6cm? s/n: ")

    print("")

    if largura == "s":
        print("peca aprovada!")

    else:
        print("reprovado! problema na largura")

else:
    print("reprovado! problema no comprimento")

print("")
print("-------------------------------")
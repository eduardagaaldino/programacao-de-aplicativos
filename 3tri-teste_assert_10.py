def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else: 
        return "Quente"

assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável"
# assert classificar_temperatura(25) == "Quente"
# assert classificar_temperatura(26) == "Frio"
# assert classificar_temperatura(26) == "Agradavel"
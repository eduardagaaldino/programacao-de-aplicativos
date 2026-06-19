temperatura = float(input("digite a temperatura atual:"))

if temperatura >= 80:
    print("PERIGO! desligando servidor por superaquecimento.")
elif temperatura >= 50:
    print("Alerta: ventoinhas ligadas no maximo!")
elif temperatura < 50:
    prin("Temperatura estavel, sistema operando normalmente.")

def eh_par(numero):
    return numero % 2 == 0

#número par positivo
assert eh_par(10) == True

#número ímpar positivo
assert eh_par(7) == False

#zero
assert eh_par(0) == True

#número negativo
assert eh_par(-4) == True
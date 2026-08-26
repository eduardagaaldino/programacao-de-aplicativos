def dobrar(numero):
    return numero * 2

#passa
assert dobrar(3) == 6
#falha (o resultado eral seria 0, por isso ele nao passa )
assert dobrar(0) == 1  
#pasaa
assert dobrar(-2) == -4

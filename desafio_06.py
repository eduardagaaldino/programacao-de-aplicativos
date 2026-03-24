print("\n -------O Sistema de Controle de Acesso-------")

autorizados =  ["Alice", "Bob", "Carlos"]
print(f"\n {autorizados}")

pesquisador = input("digite o nome de um pesquisador: ")

if pesquisador in autorizados:
    posicao = autorizados.index(pesquisador)
    print(f"\nAcesso Permitido! O pesquisador {pesquisador} está na posição {posicao}.")

    remover = input("deseja remover esse pesquisador da lista? (S/N): ")
    
    if remover == "s":
        autorizados.remove(pesquisador)

    else:
        print("programa finalizado")

else:
    print( f"Acesso Negado! O pesquisador {pesquisador} não foi encontrado.")

    cadastrar = input("desaja cadastrar um novo usuaruio? (s/n): ")
    if cadastrar == "s":
        autorizados.append(pesquisador)

print(f"\n a lista de autorizados atual e: {autorizados}")
print("-----------------------------------------------------------")
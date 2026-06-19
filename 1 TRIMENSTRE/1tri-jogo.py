nivel = int(input("digite seu nivel: "))
tarefas = int(input("digite as tarefas que ja foram coletados: "))

if nivel >= 20 and tarefas > 50: 
    print("Habilidade Super Salto desbloqueada!")
elif nivel > 20 and tarefas > 50: 
    print("Requisitos insuficientes para nova habilidade!")
elif nivel < 20 and tarefas > 50: 
    print("Requisitos insuficientes para nova habilidade!")
elif nivel > 20 and tarefas < 50: 
    print("Requisitos insuficientes para nova habilidade!")
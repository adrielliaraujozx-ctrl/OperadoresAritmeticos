nomePersonagem = input("Digite o nome do personagem: ")
classePersonagem = input(
    "Digite a classe do personagem: 1 - Guerreiro, 2 - Mago, 3 - Arqueiro: ")
while classePersonagem not in ["1", "2", "3"]:
    print("Classe inválida. Digite 1 para Guerreiro, 2 para Mago ou 3 para Arqueiro.")
    classePersonagem = input(
        "Digite a classe do personagem: 1 - Guerreiro, 2 - Mago, 3 - Arqueiro: ")
if classePersonagem == "1":
    classePersonagem = "Guerreiro"
    danoBase = 5
elif classePersonagem == "2":
    classePersonagem = "Mago"
    danoBase = 3
else:
    classePersonagem = "Arqueiro"
    danoBase = 4

listaInimigos = [50, 120, 300]

nivelPersonagem = 1

totalTurnos = 0

for inimigo in listaInimigos:
    print(
        f"\nO personagem {nomePersonagem} da classe {classePersonagem} está enfrentando um inimigo com {inimigo} de vida.")
    dano = danoBase ** nivelPersonagem
    turnos = inimigo // dano
    totalTurnos += turnos
    nivelPersonagem += 1
print(
    f"O personagem {nomePersonagem}, da classe {classePersonagem} de nivel final {nivelPersonagem} derrotou todos os inimigos em {totalTurnos} turnos.")

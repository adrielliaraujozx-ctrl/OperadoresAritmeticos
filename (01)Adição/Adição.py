quantidade_candidatos = int(input("Digite a quantidade de candidatos: "))
while quantidade_candidatos < 1 or quantidade_candidatos > 5:
    print("Quantidade de candidatos inválida. Digite um valor entre 1 e 5.")
    quantidade_candidatos = int(input("Digite a quantidade de candidatos: "))

candidatos = []

for i in range(quantidade_candidatos):
    nomes_candidatos = input(f"Digite o nome do candidato {i+1}: ")
    candidatos.append(nomes_candidatos)

votos = [0] * quantidade_candidatos

eleitores = int(input("Digite a quantidade de eleitores: "))
for i in range(eleitores):
    for j in range(quantidade_candidatos):
        print(f"{j+1} - {candidatos[j]}")
    voto = int(
        input(f"Eleitor {i+1}, digite o número do candidato que deseja votar: "))
    while voto < 1 or voto > quantidade_candidatos:
        print("Voto inválido. Digite um número válido.")
        voto = int(
            input(f"Eleitor {i+1}, digite o número do candidato que deseja votar: "))
    votos[voto-1] += 1

total_votos = sum(votos)
print("\nResultado da eleição:")
for i in range(quantidade_candidatos):
    if total_votos == 0:
        porcentagem = 0
    else:
        porcentagem = (votos[i] / total_votos) * 100

    print(f"{candidatos[i]}: {votos[i]} votos ({porcentagem:.2f}%)")

maior = max(votos)
vencedores = []
for i in range(quantidade_candidatos):
    if votos[i] == maior:
        vencedores.append(candidatos[i])
if len(vencedores) > 1:
    print("Houve um empate entre os candidatos:")
    for vencedor in vencedores:
        print(vencedor)
else:
    print(f"O vencedor da eleição é: {vencedores[0]}")
nome = []
quantidade = []
preco = []

for i in range(3):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    nome.append(nome_produto)

    quantidade_produto = int(input(f"Digite a quantidade do produto {i+1}: "))
    while quantidade_produto < 0:
        print("Quantidade inválida. Digite um valor maior ou igual a 0.")
        quantidade_produto = int(
            input(f"Digite a quantidade do produto {i+1}: "))
    quantidade.append(quantidade_produto)

    preco_produto = float(input(f"Digite o preço do produto {i+1}: "))
    while preco_produto < 0:
        print("Preço inválido. Digite um valor maior ou igual a 0.")
        preco_produto = float(input(f"Digite o preço do produto {i+1}: "))
    preco.append(preco_produto)

vendas = int(input("Digite a quantidade de vendas serao simuladas: "))
total_arrecadado = 0
for i in range(vendas):
    for j in range(3):
        print(
            f"{j+1} - {nome[j]} (Quantidade: {quantidade[j]}, Preço: R${preco[j]:.2f})")
    escolha_produto = int(
        input(f"Venda {i+1}, digite o número do produto que deseja vender: "))
    while escolha_produto < 1 or escolha_produto > 3:
        print("Escolha inválida. Digite um número válido.")
        escolha_produto = int(
            input(f"Venda {i+1}, digite o número do produto que deseja vender: "))
    quantidade_vendida = int(
        input(f"Digite a quantidade vendida do produto {nome[escolha_produto-1]}: "))
    if quantidade_vendida <= quantidade[escolha_produto-1]:
        quantidade[escolha_produto-1] -= quantidade_vendida
        total_arrecadado += quantidade_vendida * preco[escolha_produto-1]
        print(
            f"Venda realizada com sucesso! Total arrecadado: R${total_arrecadado:.2f}")
    else:
        print(
            f"Quantidade insuficiente em estoque. Estoque atual: {quantidade[escolha_produto-1]}")

for i in range(3):
    if quantidade[i] < 5:
        print(
            f"Atenção! O produto {nome[i]} está com estoque baixo. Quantidade atual: {quantidade[i]}")

print(f"\nTotal arrecadado: R${total_arrecadado:.2f}")

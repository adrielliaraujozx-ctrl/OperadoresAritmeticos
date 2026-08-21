valorSaque = int(
    input("Digite o valor do saque que deseja sacar (entre 1 e 2000): "))
while valorSaque <= 0 or valorSaque % 2 != 0 or valorSaque > 2000:
    print("Valor inválido. Digite um valor entre 1 e 2000, múltiplo de 2.")
    valorSaque = int(
        input("Digite o valor do saque que deseja sacar (entre 10 e 600): "))

cedulas = [200, 100, 50, 20, 10, 5, 2]

totalSaque = valorSaque

for cedula in cedulas:
    quantidadeCedulas = valorSaque // cedula
    valorSaque = valorSaque % cedula
    if quantidadeCedulas > 0:
        print(f"{quantidadeCedulas} cédula(s) de R$ {cedula},00")

print(f"\nTotal sacado: R$ {totalSaque},00")
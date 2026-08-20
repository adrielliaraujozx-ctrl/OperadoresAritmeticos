numeroMultiplicador = int(
    input("Digite o número que deseja ser o multiplicador: "))
numeroInicio = int(input("Digite o número inicial da tabuada: "))
while numeroInicio < 1 or numeroInicio > 10:
    print("Número inicial inválido. Digite um valor entre 1 e 10.")
    numeroInicio = int(input("Digite o número inicial da tabuada: "))
fimNumero = int(input("Digite o número final da tabuada: "))
while fimNumero < numeroInicio or fimNumero > 10:
    print("Número final inválido. Digite um valor maior ou igual ao número inicial e menor ou igual a 10.")
    fimNumero = int(input("Digite o número final da tabuada: "))

total = 0

for i in range(numeroInicio, fimNumero + 1):
    multiplicado = numeroMultiplicador * i
    print(f"{numeroMultiplicador} x {i} = {multiplicado}")
    verificar = multiplicado % 2
    if verificar == 0:
        print(f"{multiplicado} é par.")
    else:
        print(f"{multiplicado} é ímpar.")
    verificarMultiplo = multiplicado % 5
    if verificarMultiplo == 0:
        print(f"{multiplicado} é múltiplo de 5.")
    else:
        print(f"{multiplicado} não é múltiplo de 5.")
    total += multiplicado

print(f"Total acumulado até agora: {total}")

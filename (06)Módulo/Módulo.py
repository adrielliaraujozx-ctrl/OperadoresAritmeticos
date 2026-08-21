mensagem = str(input("Digite a mensagem: "))
numeroDeslocamento = int(input("Digite o número de deslocamento: "))
while numeroDeslocamento < 1 or numeroDeslocamento > 25:
    print("Número de deslocamento inválido. Digite um valor entre 1 e 25.")
    numeroDeslocamento = int(input("Digite o número de deslocamento: "))
mensagemCriptografada = ""
for letra in mensagem:
    if letra.isalpha():
        codigoAscii = ord(letra)
        if letra.isupper():
            codigoAscii = (codigoAscii - 65 + numeroDeslocamento) % 26 + 65
        else:
            codigoAscii = (codigoAscii - 97 + numeroDeslocamento) % 26 + 97
        letraCifrada = chr(codigoAscii)
        mensagemCriptografada += letraCifrada
    else:
        mensagemCriptografada += letra
print(f"\nMensagem criptografada: {mensagemCriptografada}")

perguntar = str(input("\nDeseja descriptografar a mensagem? (S/N): "))
while perguntar.upper() != "S" and perguntar.upper() != "N":
    print("Opção inválida. Digite 'S' para sim ou 'N' para não.")
    perguntar = str(input("\nDeseja descriptografar a mensagem? (S/N): "))
if perguntar.upper() == "S":
    mensagemDescriptografada = ""
    for letra in mensagemCriptografada:
        if letra.isalpha():
            codigoAscii = ord(letra)
            if letra.isupper():
                codigoAscii = (codigoAscii - 65 - numeroDeslocamento) % 26 + 65
            else:
                codigoAscii = (codigoAscii - 97 - numeroDeslocamento) % 26 + 97
            letraDecifrada = chr(codigoAscii)
            mensagemDescriptografada += letraDecifrada
        else:
            mensagemDescriptografada += letra
    print(f"\nMensagem descriptografada: {mensagemDescriptografada}")
    if mensagemDescriptografada == mensagem:
        print("A mensagem descriptografada é igual à mensagem original.")
    else:
        print("A mensagem descriptografada é diferente da mensagem original.")

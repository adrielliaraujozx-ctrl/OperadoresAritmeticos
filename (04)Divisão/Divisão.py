quantidadeAlunos = int(input("Digite a quantidade de alunos: "))
while quantidadeAlunos < 1 or quantidadeAlunos > 50:
    print("Quantidade inválida. Digite um valor entre 1 e 50.")
    quantidadeAlunos = int(input("Digite a quantidade de alunos: "))
notas = []
for i in range(quantidadeAlunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    while nota < 0 or nota > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
mediaTurma = sum(notas) / quantidadeAlunos
print(f"A média da turma é: {mediaTurma:.2f}")
maiorNota = max(notas)
print(f"A maior nota da turma é: {maiorNota:.2f}")
menorNota = min(notas)
print(f"A menor nota da turma é: {menorNota:.2f}")
quantidadeReprovados = sum(1 for nota in notas if nota < 5)
print(f"A quantidade de alunos reprovados é: {quantidadeReprovados}")
QuantidadeAprovados = quantidadeAlunos - quantidadeReprovados
print(f"A quantidade de alunos aprovados é: {QuantidadeAprovados}")
quantidadeNotasAcimaMedia = sum(1 for nota in notas if nota > mediaTurma)
print(
    f"A quantidade de alunos com nota acima da média é: {quantidadeNotasAcimaMedia}")
print("\nHistograma de notas:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {'*' * int(nota)} ({nota:.1f})")

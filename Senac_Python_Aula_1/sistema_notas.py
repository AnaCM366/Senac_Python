nomeDoAluno = input("Informe o nome do Aluno:")

nomeDaDisciplina = input("Informe o nome da Disciplina:")

nomeDoProfessor = input("Informe o nome do Professor:")

notas = []

while len(notas) < 4:
    notas.append(float(input(f'Digite a nota {i + 1}: ')))
    if notaAtual < 0 or notaAtual > 10:


for i in range(4):
    totalFinal  = totalFinal + notas[1]

media = sum(notas) / len(notas)

print(f" {aluno} {disciplina} {professor}.")
print("media", media)

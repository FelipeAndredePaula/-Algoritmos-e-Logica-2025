alunos = int(input("Digite a quantidade de alunos na turma: "))
soma_das_notas = 0
for i in range(1, alunos+1):#como o range começará no segundo valor ajustamos a delimitador de fim para +1
    nota = float(input(f"Digite a nota do {i}° aluno: "))
    soma_das_notas = soma_das_notas+nota
media = soma_das_notas / alunos
print(f"==============================\nA média da turma é de {media:.2f}")


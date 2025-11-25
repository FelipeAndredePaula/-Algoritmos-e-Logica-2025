NUM_PROVAS = 3
NUM_ALUNOS = 5
#A variável "matriz_notas" desta forma para que o Python entenda que a usaremos com uma lista.
matriz_notas = []
#Utilizamos uma "f-string" para facilitar a formatação da mesma.
print(f"--- Entrada de Notas para 3 Provas de 5 Alunos ({NUM_PROVAS}x{NUM_ALUNOS}) ---")
#Loop FOR para iterar sobre o número de provas (3).
for i in range(NUM_PROVAS):
    #Criação de um vetor vazio.
    linha_provas = []
    #Print para nos indicar qual das provas estamos manipulando.
    print(f"\n[{i + 1}ª PROVA ]")
    #Segundo loop FOR para adicionarmos as notas de cada aluno ao nosso vetor "linha_provas".
    for j in range(NUM_ALUNOS):
            #Pedimos ao usuário a nota na prova Y do aluno X, depois convertemos esse valor em um n° decimal.
            nota = float(input(f"Digite a nota do Aluno {j + 1} (Posição [{i}][{j}]): "))
            #Utilizamos o método .append() para adicionar a nota X do aluno Y na última posição do nosso vetor "linha_provas".
            linha_provas.append(nota)
    #Utilizamos novamente o .append() para desta vez adicionar o vetor todo à nossa variável "matriz_notas".
    matriz_notas.append(linha_provas)
# "\n" quebra a linha. Print para nos indicar que saímos do loop.
print("\n--- Matriz de Notas Registrada ---")
#Print com loop para exibirmos a matriz que criamos.
print("Organização: [Prova] [Aluno]")
#Loop para iterar sobre o número de provas.
for i in range(NUM_PROVAS): 
    #O argumento 'end=""' faz com que o próximo print seja feito logo após este, evitando a quebra de linha automática.
    print(f"Prova {i + 1}: ", end="")
    #Loop para iterar sobre os alunos.
    for j in range(NUM_ALUNOS): 
        #Utilizamos uma "f-string" para formatar em duas casas decimais o valor printado. O argumento 'end="\t"' simula um TAB. 
        print(f"{matriz_notas[i][j]:.2f}", end="\t")
    #Quebra a linha ao exibir todas as notas de determinada prova.
    print() 
#Criamos uma função que recebe como argumento o valor classificado como "quantidade".
def ler_notas(quantidade):
  #Lista vazia criada.
  notas = []
  #Loop para receber valores e os atribuir a variável tipo lista "notas".
  print(f"\n--- Leitura de {quantidade} Notas ---")
  for i in range(quantidade):
      nota = float(input(f"Digite a Nota {i + 1}: "))
      notas.append(nota)
  return notas
#Criamos uma segunda função que recebe como argumento o valor classificado como "lista_notas".
def analisar_notas(lista_notas):
  #Criação de variáveis acumuladoras.
  soma = 0.0
  maior_nota = 0.0
  #Loop para somar todos os valores do argumento fornecido e definir o maior deles.
  for nota in lista_notas:
    soma += nota
    if nota > maior_nota:
      maior_nota = nota
  #Calcula a média
  media = soma / len(lista_notas)
  return media, maior_nota

# --- Programa Principal ---
#Definição dos argumentos e chamada das funções para exibirmos no final do programa os valores: Lista de Notas Lida, Média Calculada e Maior Nota Alcançada
quantidade_alunos = 4
vetor_de_notas = ler_notas(quantidade_alunos)
media_final, nota_maxima = analisar_notas(vetor_de_notas)
print("\n--- Resultados da Análise ---")
print(f"Lista de Notas Lida: {vetor_de_notas}")
print(f"Média Calculada: {media_final:.2f}")
print(f"Maior Nota Alcançada: {nota_maxima:.2f}")
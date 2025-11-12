# Importante: Criamos a lista com um tamanho fixo (simulando a alocação)
TAMANHO_VETOR = 5
# Inicializamos as 5 posições com strings vazias para RESERVAR ESPAÇO NA MEMÓRIA
"""
Quando atribuímos o valor do tipo string vazio entre colchetes o Python interpreta a variável "vetor_nomes" como uma lista. Quando 
multiplicamos a atribuição de valor por "TAMANHO_VETOR", que neste caso representa o valor numérico "5", o Python itera esta 
atribuição cinco vezes, criando uma lista com cinco índices de valores iguais.
"""
vetor_nomes = [""] * TAMANHO_VETOR # vetor de palavras
print("--- Entrada de Nomes (5 Posições Fixas) ---")
# --- Primeiro FOR: Leitura e Atribuição por Índice ---
"""
No loop FOR utilizamos a função "range()" para repetir o código de bloco do loop pelo valor de "TAMANHO_VETOR". Vale notar que
quando se referimos ao primeiro aluno, e usamos "i" para isto, é necessário adicionar +1 ao seu valor. Isto se deve ao fato do Py-
thon ser "zero-based indexing".
"""
for i in range(TAMANHO_VETOR):
    # Solicitamos o nome
    nome = input(f"Digite o nome do Aluno {i + 1} (Posição [{i}]): ")
    #Atribuímos o valor "nome" para o índice em questão da lista
    vetor_nomes[i] = nome

print("\n--- Processamento dos Dados ---")
print("Os nomes registrados, acessados por índice:")
#Neste segundo loop FOR percorreremos a lista "vetor_nomes" e exibiremos o valor de cada um de seus índices.
# --- Segundo FOR: Exibição e Processamento (Acessando por Índice) ---
for i in range(TAMANHO_VETOR):
    # Acessamos o elemento pelo índice para exibição
    nome_atual = vetor_nomes[i]
    #Exibimos o valor no índice[i] da lista "vetor_nomes"
    print(vetor_nomes[i])
# Definimos o tamanho fixo do nosso vetor (simulação de alocação de memória)
TAMANHO_VETOR = 5
# 1. Pré-alocação do vetor (reserva 5 espaços, inicializando com 0.0)
vetor_notas = [0.0] * TAMANHO_VETOR
soma_notas = 0.0  # Variável acumuladora
media = 0.0       # Variável para o cálculo final
print("--- Entrada de 5 Notas ---")
# --- Primeiro FOR: Leitura e Atribuição por Índice ---
# O laço itera de 0 até 4, que são os índices válidos.
for i in range(TAMANHO_VETOR):
    # Solicitamos a nota. Usamos i+1 apenas para exibir 'Nota 1', 'Nota 2', etc.
    nota = float(input(f"Digite a Nota {i + 1} (Posição [{i}]): "))
    # Atribuímos diretamente ao índice, como em C/Java: vetor[i] = valor. Isso é diferente de usar o método ".append" pois o .append adiciona um valor no
    #final de uma lista, já no nosso caso estamos atribuindo um valor a um índice específico da lista.
    vetor_notas[i] = nota
print("\n--- Processamento dos Dados ---")
# --- Segundo FOR: Soma e Acumulação (Percorrendo o Vetor) ---
# Usamos o índice 'i' para garantir que percorremos as 5 posições. Neste segundo loop adicionamos o valor de cada índice da lista na variável "soma_notas".
for i in range(TAMANHO_VETOR):
    # Acessamos o elemento pelo índice e somamos ao acumulador.
    soma_notas = soma_notas + vetor_notas[i]
# 2. Cálculo Final da Média com estrutura condicional para verificar se o vetor está vazio antes de iniciar os cálculos.
if TAMANHO_VETOR > 0:
    media = soma_notas / TAMANHO_VETOR
# 3. Exibição dos Resultados com formatação de string para que os valores sejam exibidos somente até a segunda casa decimal (:.2f).
print(f"Vetor de Notas Registrado: {vetor_notas}")
print(f"Soma Total das Notas: {soma_notas:.2f}")
print(f"Média Final da Turma: {media:.2f}")
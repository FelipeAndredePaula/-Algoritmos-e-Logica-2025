print("Análise de Dados de Produção\n================================".upper())
n_pecas = int(input("Digite a quantidade de peças a serem analisadas: "))
tolerancia_aceitavel = 0.5
tamanho_ideal = 15
soma_dos_tamanhos = 0
pecas_fora_tolerancia = 0
for i in range(1, n_pecas+1):
    tamanho_medido = float(input(f"Digite o tamanho medido da {i}ª peça: "))
    soma_dos_tamanhos += tamanho_medido
    desvio_absoluto = abs(tamanho_medido - tamanho_ideal)
    if desvio_absoluto > tolerancia_aceitavel:
        pecas_fora_tolerancia += 1
media_tamanho_pecas = soma_dos_tamanhos / n_pecas
print("================================")
if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")
print(f"Média de tamanho das peças: {media_tamanho_pecas:.2f}\nQuantidade\
 de peças fora da tolerância: {pecas_fora_tolerancia}")
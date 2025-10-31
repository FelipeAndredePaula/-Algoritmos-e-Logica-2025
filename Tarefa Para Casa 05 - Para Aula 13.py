"""
Diferente do loop FOR onde definimos de antemão o número de vezes que um determinado bloco de código será executado, no
loop WHILE tal bloco de código será executado inúmeras vezes enquanto uma condição definida de antemão permaneça verdadeira.
"""
print("Análise de Dados de Produção com loop while\n================================".upper())
tolerancia_aceitavel = 0.5
tamanho_ideal = 15
soma_dos_tamanhos = 0
pecas_fora_tolerancia = 0
n_pecas = 0
i = True
while i == True:#Definição da condição para iterar novamente o bloco de código do WHILE ou não.
    tamanho_medido = float(input(f"Digite o tamanho medido da peça: "))
    soma_dos_tamanhos += tamanho_medido
    desvio_absoluto = abs(tamanho_medido - tamanho_ideal)
    if desvio_absoluto > tolerancia_aceitavel:
        pecas_fora_tolerancia += 1
    n_pecas += 1
    resposta = input("Deseja informar o tamanho medido de outra peça? (SIM ou NÃO): ").upper()
    if resposta == "NÃO":
        i = False#Muda o valor de "i" para que não haja uma nova iteração do bloco de código do WHILE.
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
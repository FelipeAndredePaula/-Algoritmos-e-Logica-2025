def exibir_cabecalho(titulo, simbolo):
    linha_separacao = simbolo * 20
   
    print(linha_separacao)
    print(f"{titulo}".upper())
    print(linha_separacao)
# 1ª Chamada: Título e Símbolo '#'
exibir_cabecalho("Relatório Mensal", "#")
# Adiciona uma linha em branco para separar visualmente
print()
# 2ª Chamada: Título e Símbolo '*'
exibir_cabecalho("Resultado", "*")
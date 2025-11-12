print("Cadastro e Listagem de Notas da Turma\n========================".upper())
lista_notas = []
n_notas = 5
for i in range(n_notas):
    nota = float(input(f"Digite o valor da {i+1}ª nota: "))
    lista_notas.append(nota)
print("========================")
for i in range(len(lista_notas)):
    print(f"Valor da {i+1}ª nota: {lista_notas[i]}")
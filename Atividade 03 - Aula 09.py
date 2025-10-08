simbolo = input("Digite um símbolo (por exemplo #, !, @): ")
repeticao = int(input("Digite quantas vezes (número inteiro diferente de 0) o símbolo deverá ser repetido: "))
if repeticao != 1:
    print(f"================================\nRepetindo o símbolo {simbolo} {repeticao} vezes...")
else:
    print(f"================================\nRepetindo o símbolo {simbolo} apenas uma única vez...")
for i in range(repeticao):
    print(simbolo)
print("Fim da repetição")
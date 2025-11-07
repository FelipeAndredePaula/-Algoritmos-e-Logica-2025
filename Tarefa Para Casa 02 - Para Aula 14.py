print("Somatória de Pares até o Zero\n=====================".upper())
soma_pares = 0
num_digitado = 1
while num_digitado != 0:
    num_digitado = int(input("Digite um número inteiro ('0' para encerrar): "))
    if num_digitado == 0:
        print("Valor '0' digitado, encerrando o loop.")
    elif num_digitado % 2 == 0:
        soma_pares += num_digitado
        print("Valor adicionado a soma dos nº pares.")
    else:
        print("Número ímpar digitado, ignorando...")
print(f"=====================\nA soma total dos números pares digitados é: {soma_pares}")

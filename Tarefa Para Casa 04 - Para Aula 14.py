print("Somatória Separada de Pares e Ímpares até o usuário digitar Zero\n==============================".upper())
soma_pares = 0
soma_impares = 0
numero_digitado = 1
while numero_digitado != 0:
    numero_digitado = int(input("Digite um valor inteiro (0 para encerrar): "))
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            soma_pares += numero_digitado
            print(f"{numero_digitado} é par, acumulando o valor...")       
        else:
            soma_impares += numero_digitado
            print(f"{numero_digitado} é ímpar, acumulando o valor...")
    else:
        print("Valor de parada inserido, encerrando o loop...")
print(f"==============================\nA soma total dos números pares é: {soma_pares}\nO soma total dos números ímpares é: {soma_impares}") 

        
print("Contagem de Pares e Ímpares até o Zero\n==============================".upper())
contador_pares = 0
contador_impares = 0
numero_digitado = 1
while numero_digitado != 0:
    numero_digitado = int(input("Digite um valor inteiro (0 para encerrar): "))
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            contador_pares += 1
            print(f"{numero_digitado} é par...")       
        else:
            contador_impares += 1
            print(f"{numero_digitado} é ímpar...")
    else:
        print("Valor de parada inserido, encerrando o loop...")
print(f"==============================\nO total de números pares digitados é: {contador_pares}\nO total de números ímpares digitados é: {contador_impares}")     
        
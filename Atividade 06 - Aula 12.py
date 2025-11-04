print("TABUADA DE NÚMERO INTEIRO DO 1-10.\n===============================")
tabuada = int(input("Digite o número inteiro que você gostaria de ver a tabuada: "))
contador = 1
while contador < 11:
    result =  tabuada*contador
    print(f"{tabuada}x{contador} = {result}")
    contador += 1
print("===============================\nTABUADA COMPLETA.")

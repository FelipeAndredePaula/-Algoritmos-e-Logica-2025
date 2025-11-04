car = input("Digite um caractere ou símbolo (ex: *, #, -): ")
repetir = "sim"
while repetir == "sim":
    for i in range(20):
        print(car, end='')  # sem espaço nem nova linha
    repetir = input("\nDeseja ver outra linha?(caso queira, digite 'sim'): ".lower())
print("Gerador encerrado. Obrigado!")
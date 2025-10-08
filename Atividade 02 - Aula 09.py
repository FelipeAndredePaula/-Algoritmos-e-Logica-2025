numero_usuario = int(input("Digite um número inteiro: "))
print("=====================================")
print(f"TABUADO DO {numero_usuario}")
for num in range(1, 11):
    mult = numero_usuario*num
    print(f"{numero_usuario}x{num} = {mult}")
print("FIM DA TABUADA")
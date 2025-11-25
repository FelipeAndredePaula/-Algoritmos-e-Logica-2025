NUM_ITENS = 3
cardapio = []
print("--- Entrada de Dados para Cardápio (3 Itens) ---")
for i in range(NUM_ITENS):
    print(f"\n[ Item {i + 1} ]")
  
    nome = input("  Digite o nome do item: ")
    preco = float(input("  Digite o preço do item: R$ "))
   
    item_completo = [nome, preco]
   
    cardapio.append(item_completo)
print("\n--- Acessando Elementos Específicos ---")
preco_item2 = cardapio[1][1]
print(f"O preço do Item 2 (posição [1][1]) é: R$ {preco_item2:.2f}")
nome_item3 = cardapio[2][0]
print(f"O nome do Item 3 (posição [2][0]) é: {nome_item3}")
print("\n--- Exibição do Cardápio Completo ---")
for item in cardapio:
    print(f"Nome: {item[0]} | Preço: R$ {item[1]:.2f}")
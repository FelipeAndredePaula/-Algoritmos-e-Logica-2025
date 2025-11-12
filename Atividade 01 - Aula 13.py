"""
Neste bloco ocorre a criação da variável "lista_frutas" do tipo lista. Em seguida é indexado valores do tipo string à lista.
E por fim um print.
"""
lista_frutas = ["Maçã", "Banana", "Uva", "Pêra", "Manga"]

print("--- Análise da Lista ---")
"""
A seguir printa a lista criada anteriormente é exibida na tela com todos seus valores indexados. Este print apresentará os itens
entre [], com cada um separado por vírgula e aspas, pois o que está sendo printado é a variável lista como um todo, não a representa-
ção de cada um de seus valores. 
"""
print("Lista completa:", lista_frutas)
"""
A seguir a variável "primeiro" é criada. É atribuído o primeiro valor da nossa lista a variável "primeiro". Python tem a caracterís-
tica "zero-based indexing", isso quer dizer que os índices que usamos para acessar os valores dentro de uma variável são contabili-
zados a partir do 0. Ou seja, para acessar o primeiro valor da nossa lista ("Maçã") utilizamos o índice 0, para acessar o segundo 
valor ("Banana") utilizamos o índice 1, e assim por diante.
"""
# 3. Acesso ao Primeiro Elemento (Índice 0)
primeiro = lista_frutas[0]
print("1. Primeiro elemento (índice 0):", primeiro)

# 4. Acesso ao Terceiro Elemento (Índice 2)
terceiro = lista_frutas[2]
print("2. Terceiro elemento (índice 2):", terceiro)
"""
Quando utilizamos o índice [-1] para acessar um valor de uma lista, o Python acessa o último valor daquela lista que no nosso caso
é o valor ['Manga']. Da mesma forma, o índice -2 de uma lista acessa seu penúltimo valor e assim por diante.
"""
# 5. Acesso ao Último Elemento (Índice -1)
ultimo = lista_frutas[-1]
print("3. Último elemento (índice -1):", ultimo)
#Variável que representa o número de linhas (3) da nossa matriz.
NUM_LINHAS = 3
#Variável que representa o número de colunas (3) da nossa matriz.
NUM_COLUNAS = 3
#A variável "matriz" é criada. A atribuição de valor "[]" serve para indicarmos ao Python que nossa variável sera uma lista.
matriz = []
#Usamos um loop FOR para "popularmos" os valores da nossa matriz com vários zeros. Isso fará "matriz" ser uma lista com três sublistas "aninhadas".
for i in range(NUM_LINHAS):
    #O método .append adiciona o valor 0 ao final da lista. Essa operação é multiplicada X vezes, sendo X = NUM_COLUNAS. E por fim esta operação é repetida Y vezes, sendo Y = NUM_LINHAS.
    matriz.append([0] * NUM_COLUNAS)
#Usamos dois loops FOR para percorrer cada valor de cada sublista dentro da nossa variável "matriz". O loop i representa as linhas e o loop j as colunas. Desta forma é possível...
#percorrer todas as coordenadas da nossa matriz.
for i in range(NUM_LINHAS): # Loop para as linhas (i)
    for j in range(NUM_COLUNAS): # Loop para as colunas (j)
        #Solicitamos um valor ao usuário para ser inserido na respectiva coordenada. 
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        #O valor informado pelo usuário é armazenado dentro de nossa matriz.
        matriz[i][j] = valor
#No último loop repetimos a estrutura do anterior para desta vez exibirmos a matriz criada.
for i in range(NUM_LINHAS): 
    for j in range(NUM_COLUNAS):
        #Utilizamos o argumento opicional "end" do comando print para "simular" um TAB. Isso melhora a visibilidade do nosso print.
        print(matriz[i][j], end="\t")
    print() # Pula linha após cada linha da matriz. É o que da a "aparência" de matriz para nosso print.
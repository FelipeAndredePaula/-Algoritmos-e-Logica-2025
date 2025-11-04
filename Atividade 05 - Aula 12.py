"""
Neste código começamos importando o módulo "random" para lidar com geração de números aleatórios. O método ".randint" do módulo
"random" gera um número aleatório definido pelos argumentos fornecidos, neste caso do 1 até o 6, representado a ação de jogar um
dado. Depois algumas variáveis de controle são declaradas. Em seguida, o loop WHILE é criado para repetir seu bloco de código inden-
tado enquanto a condição "Not acertou" permanecer verdadeira. Dentro do loop é pedido ao usuário seu palpite, com um bloco condicio-
nal para verificar se o valor digitado está entre 1-6. Depois a variável acumuladora "tentativas" recebe +1, caso o usuário acerte
o loop se encerra e, caso ele erre, o loop se repete com mensagens apropriadas em ambos os casos. Por fim é mostrado ao usuário qual
número foi sorteado ao chamar o método ".randint" do módulo "random" e o número de tentativas.
"""
print("JOGO DE DADOS COM WHILE")
import random
# 1. Variáveis de controle
numero_secreto = random.randint(1, 6) # Sorteia o número do dado (1 a 6)
tentativas = 0
acertou = False
palpite_usuario = 0 # Inicializa com um valor para garantir que o loop comece
print("--- Jogo de Adivinhar o Dado ---")
print("Tente adivinhar o número que o dado sorteou (entre 1 e 6).")
# 2. Laço while: continua enquanto 'acertou' for False
while not acertou:
    # Solicita o palpite do usuário
    palpite_usuario = int(input("Seu palpite: "))
    # Garante que o palpite está dentro do intervalo
    if palpite_usuario < 1 or palpite_usuario > 6:
        print("Palpite fora do intervalo. Tente um número entre 1 e 6.")
        continue
    # Incrementa o contador de tentativas
    tentativas += 1
    # 3. Verifica a condição de acerto
    if palpite_usuario == numero_secreto:
        acertou = True # Altera a variável de controle para sair do loop
        print("\n*** Parabéns! Você acertou! ***")
    else:
        # Dica simples para manter o jogo ativo
        print("Errado. Tente novamente.")
# 4. Mensagem final
print(f"O número sorteado era: {numero_secreto}")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")
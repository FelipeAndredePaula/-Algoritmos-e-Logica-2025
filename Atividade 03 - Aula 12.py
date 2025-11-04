SENHA_CORRETA = "python123"
tentativas_erradas = 0
senha_digitada = ""  
"""
RESPONDA: Porque a variável senha_digitada começa com vazio, ""
RESPOSTA: Atribuir o valor "falso" para a variável "senha_digita" garante que não haja erro na chamada do loop WHILE. Caso tentar-
mos comparar o valor da variável "senha_digitada" antes de o declarar, receberemos a mensagem de erro do pylance:

--- Sistema de Login ---
Traceback (most recent call last):
  File "c:\Users\felps\Documents\Estudos\CloneGit\-Algoritmos-e-Logica-2025\Atividade 03 - Aula 12.py", line 11, in <module>
    while senha_digitada != SENHA_CORRETA:
          ^^^^^^^^^^^^^^
NameError: name 'senha_digitada' is not defined
"""

print("\n--- Sistema de Login ---")
while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == SENHA_CORRETA:
        print(f"\nSenha válida! Acesso concedido.")       
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")
print ("Total de entradas erradas", tentativas_erradas)
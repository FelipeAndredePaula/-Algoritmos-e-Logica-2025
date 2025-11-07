print("Jogo de Adivinhar o Número\n===================".upper())
import random as rd
rnum = rd.randint(1,10)
print("Um número de 1-10 foi gerado...")
acertou = False
tentativas = 0
while acertou == False:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite == rnum:
        print("Parabéns, você acertou!")
        acertou = True
    elif palpite > rnum:
        print("Seu palpite foi muito alto. Tente um número menor.")
    else:
        print("Seu palpite foi muito baixo. Tente um número maior.")
print(f"===================\nNúmero gerado aleatóriamente:\
 {rnum}\nNº de tentativas: {tentativas}")
"""
Estruturas de repetições ou, laços de repetições, são blocos de código que são rodados múltiplas vezes até que uma
condicional pré estabelecida seja atendida. Eles são muito úteis para poupar tempo e esforço do programador que 
não precisará escrever as mesmas linhas de códigos repetidas vezes. O laço de repetição "for item in iterável" é 
usado quando se sabe quantas vezes precisaremos repetir determinada instrução. Iterável é todo tipo de dado que po-
de ser percorrido elemento por elemento (sendo a repesentação de cada elemento o que vem antes de "in")
"""
#Exemplo, caso quisermos escrever todos os caractéres de uma string, um em cada linha:
string = "Python"
for letra in string:
    print(letra)

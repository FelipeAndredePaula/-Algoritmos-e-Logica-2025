#Felipe André Silva de Paula
#0220482523046
#BoaNoiteMarcus
#print("Felipe André Silva de Paula, RA 0220482523046")
#Entrada de dados
print("==================================")
print("CALCULADORA DO NÍVEL DE GLICOSE")
glicose_jejum = float(input("Digite o valor da glicose em jejum em mg/dL: "))
#Início do bloco condicional para exibir mensagem apropriada
if glicose_jejum < 100:
    print("Glicemia Normal.")
elif glicose_jejum >= 100 and glicose_jejum <= 125:
    print("Pré-diabetes: Risco Moderado.")
else:
    print("Diabetes: Nível Alto.")
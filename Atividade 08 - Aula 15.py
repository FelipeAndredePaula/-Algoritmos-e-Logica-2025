print(f"Exercício de criação de função\n============================".upper())

def somar_dois_numeros(num_1,num_2):
    return num_1+num_2

nume_1 = int(input("Digite o valor do 1° número: "))
nume_2 = int(input("Digite o valor do 2° número: "))
resultado = somar_dois_numeros(nume_1,nume_2)
print(f"============================\nA soma do 1° número ({nume_1}) com o 2° número ({nume_2}) é de: {resultado}")

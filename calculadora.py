
def adicao (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    return a / b

def porcentagem (porcentagem, valor):
    resultado = porcentagem / 100 * valor
    return resultado

print("Calculadora do Rafão")


print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Porcentgem")

operacao = int(input("\n digite a operação \n"))

while operacao <= 0 or operacao > 5:
    print("Operação Inválida")
    operacao = int(input("\n digite a operação válida \n")) 

n1 = int(input(" digite o primeiro número "))
n2 = int(input(" digite o Segundo número "))

if operacao == 1:
    print(n1, "+", n2, "=", adicao(n1, n2))
elif operacao == 2:
    print(n1, "-", n2, "=", subtracao(n1, n2))
elif operacao == 3:
    print(n1, "*", n2, "=", multiplicacao(n1, n2))
elif operacao == 4:
    print(n1, "/", n2, "=", divisao(n1, n2))
elif operacao == 5:
    print(porcentagem(n1, n2))

print("\n Cáculo Realizado com sucesso!")


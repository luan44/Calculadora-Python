nome = input("Qual é o seu nome?")
cidade = input("Qual é a sua cidade?")
idade = int(input("Qual é a sua idade?"))
while True:
    print("\n=== Calculadora ===")
    
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    operacao = input("Escolha alguma das operações (+, -, *, /) ou digite 'sair' para encerrar: ")

print("Olá,", nome ,"você tem", idade ,"anos, e mora em", cidade)


for i in range(10):
    print("Repetição", i)

contador = 0
while contador <= 10:
    print("Contador:", contador)
    contador += 1    if operacao == "+":
        print("Resultado:", n1 + n2)
    elif operacao == "-":
        print("Resultado:", n1 - n2)
    elif operacao == "*":
        print("Resultado:", n1 * n2)
    elif operacao == "/":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero.")
    else:
        print("Operação inválida!")

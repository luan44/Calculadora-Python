nome = input("Qual é o seu nome?")
cidade = input("Qual é a sua cidade?")
idade = int(input("Qual é a sua idade?"))

print("Olá,", nome ,"você tem", idade ,"anos, e mora em", cidade)


for i in range(10):
    print("Repetição", i)

contador = 0
while contador <= 10:
    print("Contador:", contador)
    contador += 1
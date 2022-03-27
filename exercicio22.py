idade = 1
altura = 0
somaidade = 0
qtdidade50 = 0

while (idade > 0):
    idade = int(input("Digite sua idade"))
    altura = float(input("Digite sua altura"))

    if idade > 50:
        somaidade = somaidade + 1
        qtdidade50 = qtdidade50 + 1
print("A media das alturas = {}".format(somaidade / qtdidade50))
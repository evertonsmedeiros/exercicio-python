
soma = 0
idade = 0
idade = float(input("digite sua idade"))

while soma < idade:
    soma = idade + 1

    if (idade <= 15):
        print("Menor de Idade ")


    elif (  idade >= 16 and idade <= 30):
        print("--- Jovem ")



    elif (  idade >= 31 and idade <= 45):
        print("meia idade ")



    elif (  idade >= 46 and idade <= 60):
        print("velho ")


    elif (  idade >= 60):
        print("mais velho que a fome")
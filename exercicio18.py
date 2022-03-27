resp = "s"
idade = 0
qtdgrupo_salario = media_salario_grupo = 0
cont = Menor_salario = Maior_salario = 0
qtdSal2000 = 0
maior = menor = soma = qtd = 0
while resp in  "Ss":
    idade = int(input("Digite sua idade"))
    salario = float(input("Digite o seu salario"))
    sexo =  str(input("Digite o sexo --masculino ou femenino").upper().strip()[0])
    resp = str(input("quer continua s- para sim -n- para não").upper().strip()[0])

    soma += idade
    qtd += 1
    if qtd == 1:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    if(sexo == "f" and salario <=200.00):
        qtdSal2000 += sexo

    elif(salario):
        qtdgrupo_salario += 1
        media_salario_grupo = media_salario_grupo + salario
    if qtd == 1:
        maior = menor = idade
    if(idade,sexo,salario > Maior_salario):
        cont += 1
        salario = Maior_salario
    if(idade,sexo,salario < Menor_salario ):
        cont += 1
        Menor_salario = salario
Menor_salario = Menor_salario + 1
print("a idade e {} o sexo da pessoa que possui o menor sallario é {} o menor salario${}.".format(idade,sexo,Menor_salario))

print("a m ́edia dos sal ́arios do grupo é ${}".format(qtdgrupo_salario/media_salario_grupo))




qtdSal2000 = qtdSal2000 + 1
print("a quantidade de mulheres com sal ́ario at ́ ${} é ".format(qtdSal2000))

media = soma / qtd
print("a media das idades {}".format(qtd,media))
print("a maior idade foi{} e a menor idade foi {}".format(maior,menor))


sair = 5
con1 = 0
meses = 0
cont2 = 0
ççççççççç = 0
mmmm = 0
salario = 0
ferias = 0
contadorfim = decimo = 0
a = media1 = 0
b = media2 = 0
c= media3 = 0
print("Menu de opções:")
print('DIGITE --1-- Para Novo salário')
print('DIGITE --2-- Para Férias')
print('DIGITE --3-- Para Décimo terceiro')
print('DIGITE --4-- sair ou 5 para continuar')
while (sair > 4 ):
    escolha = int(input("Digite a opção do menu "))
    salario = float(input("digite seu salario"))
    sair = int(input("digite o numero 4 para sair ou 5 paracontinuar"))
    if(escolha == 1):
        con1 += 1
        if(salario < 210.00):
            a += 1
            media1 = media1 +salario
            print( media1 * 15 / 100 + salario)
        if(salario >=210.00 and salario <= 600.00):
            b += 1
            media2 = media2 + salario
            print("o seu salario teve aumento de 10%...Novo salario ${}".format(media2 * 10/100 + salario ))
        if(salario >= 600.00):
            c += 1
            media3 = media3 + salario
            print("o seu salario teve aumento de 0.5%..Novo salario ${}".format(media3 * 5/100 + salario))
        else:
            print("ok")
    if(escolha == 2 ):
        cont2 +=1
        ferias = ferias + salario
    print("o valor das férias é {}".format(ferias * 3 / 100 + ferias))


    if(escolha == 3):
        contadorfim += 1
        meses = int(input("Digite quantos meses vc trabalhou?"))
        decimo = decimo + salario
    print("o valor do seu decimo terceiro eé {}".format(decimo*meses/12+salario))







#Fa ̧ca  um  programa  que  receba  o  valor  de  um  carro  e  mostre  uma  tabela  com  os

preçoFavista = 0
avistaDesconto = 0
valorCarro = 0
parcelas1 = 0
parcelas6 = 0
p6valor1 = 0
parcela12 = 0
par12divi = 0

par_18_dividir = 0
par18 = 0

p24= 0
pdividir24 = 0
for i in range(0,1):
    valorCarro = float(input("digite ovalor do carro"))

    if(valorCarro == valorCarro):
        preçoFavista = preçoFavista + 1
        avistaDesconto = avistaDesconto + valorCarro
avistaDesconto = avistaDesconto * 20 / 100
valorCarro = valorCarro + avistaDesconto
print("o seu desconto será {}% é o valor total do carro será{}".format(avistaDesconto,valorCarro))
for i in range(0,1):
    valorCarro = float(input("digite o valor do carro para 6 parcelas"))

    if(valorCarro ):
        parcelas1 = parcelas1 + 1
        p6valor1 = p6valor1 + valorCarro
        parcelas6 = parcelas6 + valorCarro
p6valor1 = p6valor1 * 3 / 100
parcelas6 = parcelas6 / 12
valorCarro = valorCarro + p6valor1
print ("o valor da sua parcela em 6x de ${:.3f} e o valor final do carro será$${}".format(parcelas6,valorCarro))



for i in range(0,1):
    valorCarro = float(input("digite o valor do carro para 12 parcelas"))

    if(valorCarro ):
        parcelas1 = parcelas1 + 1
        parcela12 = parcela12 + valorCarro
        par12divi = par12divi + valorCarro
par12divi = par12divi * 6 / 100
parcela12 = parcela12 / 6
valorCarro = valorCarro + par12divi
print ("o valor da sua parcela será 12 x de ${:.3f} e o valor final do carro será$${}".format(parcela12,valorCarro))

for i in range(0,1):
    valorCarro = float(input("digite o valor do carro para 18 parcelas"))

    if(valorCarro ):
        parcelas1 = parcelas1 + 1
        par18 = par18 + valorCarro
        par_18_dividir = par_18_dividir + valorCarro
par_18_dividir = par_18_dividir * 9 / 100
par18 = par18 / 18
valorCarro = valorCarro + par_18_dividir
print ("o valor da sua parcela em 18 x de ${:.3f} e o valor final do carro será$${}".format(par18,valorCarro))



for i in range(0,1):
    valorCarro = float(input("digite o valor do carro para 12 parcelas"))

    if(valorCarro ):
        parcelas1 = parcelas1 + 1
        p24 = p24 + valorCarro
        pdividir24 = pdividir24 + valorCarro
pdividir24 = pdividir24 * 12 / 100
p24 = p24 / 24
valorCarro = valorCarro + par12divi
print ("o valor da sua parcela em 24 x de ${:.3f} e o valor final do carro será$${}".format(p24,valorCarro))


















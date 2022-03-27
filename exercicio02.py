#Uma companhia de teatro deseja montar uma s ́erie de espet ́aculos.  A dire ̧c ̃ao calcula
valor = 5
vendas = 120
despesas = 200
lucruInicial = (valor * vendas) - despesas
valorMaior= valor
lucroMaior= lucruInicial
vendasMaior = vendas
for i in range(valor >= 1):
    print("valor",valor)
    print("vendas",vendas)
    print("despesas",despesas)
    print("lucro inicial",lucruInicial)
    print("lucro maior",lucroMaior)
    valor = valor - 0.50
    vendas = vendas + 26
    lucruInicial = (valor * vendas) - despesas
    lucroMaior = (valor * vendas) - despesas
    if lucruInicial >= lucroMaior:
        valorMaior += valor
        vendasMaior += vendas



idade = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
opniaoFilme = ["","","","","","","","","","","","","","",""","""];
otimo = "otimo"
bom = "bom"
qtpessoasBom_ = 0
porcentagBom = 0
qtdotimo = 0
mediaidade = 0
regular = "regular"
qtdPessoas_regular = 0
qt = 0
for i in range(0,2):
    idade[i] = int(input("digite a idade da pessoa n: " + str(i + 1) + ""))  # converçao str
    opniaoFilme[i] = str(input("digite uma opiniao em relac̃ao ao filme: opçoes =  ́otimo - bom -  regular " + str(i + 1) + ""))  # converçao str


for i in range(0,15):
    if(opniaoFilme[i] == otimo ):
        qtdotimo = qtdotimo + 1
        mediaidade = mediaidade + idade[i]
if(mediaidade > 0):
    mediaidade = mediaidade / qtdotimo
    print("a m edia das idades das pessoas que responderam  ́otimo;é {}".format(mediaidade))

for i in range(0,15):
    if(opniaoFilme[i] == regular):
        qtdPessoas_regular = qtdPessoas_regular + 1

qt = qt + qtdPessoas_regular
print( "a quantidade de pessoas que responderam regular; e {}".format(qtdPessoas_regular))

for i in range(0,15):
    if(opniaoFilme[i] == bom ):
        qtpessoasBom_ = qtpessoasBom_ + 1
        porcentagBom = porcentagBom +  idade[i]

porcentagBom = porcentagBom * qtpessoasBom_ / 100
print("A percentagem de pessoas que responderam bom é,{}".format(porcentagBom))


















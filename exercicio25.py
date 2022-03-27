print("------Escolha uma opção do Menu------")
opçao = 0
continuar = "c"
fundosDerenda = contrenda = 0
poupançaPlus = contplus = 0
poupança = contP = 0
while continuar in "Cc":
    opçao = int(input("Digite -1- para poupança, --2--para poupança plus, -3- para fundos de renda fixa  "))
    valorinvestimento = float(input("Digite o valor do seu investimento"))
    continuar = str(input("Digite --C-- Para continuar"))
    if(opçao == 1):
        contP += 1
        poupança = poupança + valorinvestimento
        print("O valor do seu investimento, na poupança é{} ".format(poupança*1.5/100+valorinvestimento))
    else:

        if(opçao == 2):
            contplus +=1
            poupançaPlus = poupançaPlus + valorinvestimento
        print("o valor do seu investimento, na poupança plus é {}".format(poupançaPlus *2/100+valorinvestimento))

    if(opçao == 3 ):
        contrenda += 1
        fundosDerenda = fundosDerenda + valorinvestimento
        print("o valor do seu investimento no Fundo de renda fixa é".format(fundosDerenda*4/100+valorinvestimento))








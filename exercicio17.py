pessoas = 1
cont = 0
qtdcanal4 = 0
media4 = 0
qtd5 = 0
mediac5 = 0
canal = 0
qtd_canal_5 = 0
while(pessoas > 0):
    pessoas = int(input("Digite quantas pessoas estavam assistindo na sua casa"))
    canal = int(input("digite o numero do canal que estava assistindo"))

    if(pessoas >= 0):
        cont = cont + pessoas
        print("o numero de quantidade de pessoas assistindo é ={}".format(cont))

        if( canal == 4):
            qtdcanal4 = qtdcanal4 + 1
            media4 = media4 + pessoas
            print("A porcentagem de pessoas assistindo o canal 4 é {}".format(qtdcanal4 / media4))

        while (pessoas > 0):

            if (canal == 5):
                qtd_canal_5 = qtd_canal_5 + 1
                mediac5 = mediac5 + pessoas
                print(mediac5)















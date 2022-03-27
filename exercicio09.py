#9.  Fa ̧ca um programa que receba dez idades, pesos e alturas, calcule e mostre:
idade = [0,0,0,0,0,0,0,0,0,0]
mediaidade = 0
qtdpessoas_acima_90 = 0
qtdpessoas_entr10_30Anos = 0
qtd_medem_mais_de_190 = 0
qtd10_pessoas = 0

altura = [0,0,0,0,0,0,0,0,0,0]
mediaAltura = 0
qtdpessoasEntre1030 = 0


peso = [0,0,0,0,0,0,0,0,0,0]
qtdPeso_acima_90kg = 0
qtdAlturaInferior1_50 = 0

for i in range(0,10):
    idade[i] = int(input("digite a idade da pessoa n:"+ str(i+1) +" "))
    peso[i] = float(input("digite o peso da pessoa n: " + str(i + 1) + ""))
    altura[i] = float(input("digite sua altura da pessoa n:" + str(i + 1) + " "))
#a mdas idades das dez pessoas;
for i in range(0,10):
    qtd10_pessoas = qtd10_pessoas + 1
    mediaidade = mediaidade + idade[i]
    mediaidade = mediaidade / qtd10_pessoas
print("a media das idades das 10 pessos é {} ".format(mediaidade))

#a quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro;
for i in range(0,10):
    if(peso[i] >= 90 and altura[i] <= 1.50 ):
        qtdpessoas_acima_90 = qtdPeso_acima_90kg + 1
        qtdAlturaInferior1_50 = qtdAlturaInferior1_50 + 1
qtdPeso_acima_90kg = qtdPeso_acima_90kg + qtdAlturaInferior1_50
print("a quantidade de pessoas com peso maior que 90kg e altura inferior a 1.50 maetros é {}".format(qtdPeso_acima_90kg))

#quantidade de pessoas > 10 < 30 anos
for i in range(0,10):
    if(idade[i] >=10 and idade[i] <= 30, altura[i] >= 1.90  ):
        qtdpessoasEntre1030 = qtdpessoasEntre1030 + 1
        mediaAltura = mediaAltura + idade[i] and altura[i]
mediaAltura = mediaAltura / qtdpessoasEntre1030
print("media da altura depessoas entre 10  e 20 anos {}".format(mediaAltura))
        



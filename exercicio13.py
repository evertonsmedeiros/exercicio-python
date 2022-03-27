#Fa ̧ca um programa que receba a idade e o peso de quinze pessoas, e que calcule e
idade = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qtdpessoas1_10 = 0
medipeso1_10 = 0
qtdEntre11_20_anos = 0
media11_20_ANOA = 0
qtdEntre21_30_anos = 0
media_21_30 = 0
qtdAcimaD50_Anos = 0
media50 = 0

peso = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,15):
    idade[i] = int(input("digite a idade da pessoa n: " + str(i + 1) + ""))
    peso[i] = float(input("digite o pesp  da pessoa n: " + str(i + 1) + ""))
    #media peso da idade entre 1 10 anos
for i in range(0,15):
    if(idade[i] >=1 and idade[i] <= 10  ):
        qtdpessoas1_10 = qtdpessoas1_10 + 1
        medipeso1_10 = medipeso1_10 + peso[i]
medipeso1_10 = medipeso1_10 / qtdpessoas1_10
print("media do peso das pessoas entre 1 e 10 anos n {}".format(medipeso1_10))
  #entre 11 e 20
for i in range(0,15):
    if(idade[i] >=11 and idade[i] <= 20  ):
        qtdEntre11_20_anos = qtdEntre11_20_anos + 1
        media11_20_ANOA = media11_20_ANOA + peso[i]
media11_20_ANOA = media11_20_ANOA / qtdEntre11_20_anos
print("media do peso das pessoas entre 11 e 20 anos n {}".format(media11_20_ANOA))

#media dopeso entre 21 e 30 anos
for i in range(0,15):
    if(idade[i] >=21 and idade[i] <= 30  ):
        qtdEntre21_30_anos = qtdEntre21_30_anos + 1
        media_21_30 = media_21_30 + peso[i]
media_21_30 = media_21_30 / qtdEntre21_30_anos
print("media do peso das pessoas entre 21 a 30 anos n {}".format(media_21_30))

#media acima dos 50 anos
for i in range(0,15):
    if(idade[i] >= 50  ):
        qtdAcimaD50_Anos = qtdAcimaD50_Anos + 1
        media50 = media50 + peso[i]
media50 = media50 / qtdAcimaD50_Anos
print("media do peso das pessoas acima dos 50 anos é {}".format(media50))
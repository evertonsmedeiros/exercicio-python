
idade = [0,0,0,0,0,]
altura = [0.0,0.0,0.0,0.0,0.0]
peso = [0.0,0.0,0.0,0.0,0.0]
qtdpessoasAcimados50 = 0
qtdpessoasEntre1020 = 0
mediaAltura = 0.0
pessoasMenos40kg = 0
mediaPeso = 0
qtdPolhosAzuis = 0
for i in range(0, 5):


    idade[i] = int(input("digite a idade da pessoa n: "+ str(i+1)+""))
    altura[i] = float(input("digite sua altura da pessoa n:"+ str(i+1)+" "))
    peso[i] = float(input("digite o peso da pessoa n: "+str(i+1)+""))

for elementos in idade:
    if(elementos >= 50):
        qtdpessoasAcimados50 = qtdpessoasAcimados50 + 1
print("quantidade de pessoas acima dos 50 anos{} ".format(qtdpessoasAcimados50))


for i in range(0,5):
    if(idade[i] >=10 and idade[i] <= 20  ):
        qtdpessoasEntre1020 = qtdpessoasEntre1020 + 1
        mediaAltura = mediaAltura + altura[i]
mediaAltura = mediaAltura / qtdpessoasEntre1020
print("media da altura depessoas entre 10  e 20 anos {}".format(mediaAltura))

for i in range(0,5):
    if(peso[i] <= 40  ):
        pessoasMenos40kg = pessoasMenos40kg + 1
        mediaPeso = mediaPeso + altura[i]
mediaAltura = mediaAltura / pessoasMenos40kg
print("a  porcentagem  de  pessoas  com  peso  inferior  a   kg{}".format(mediaPeso))






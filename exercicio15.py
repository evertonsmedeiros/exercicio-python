resposta = ["","","","","","","","","",""]
sexo = ["","","","","","","","","",""]

masculino = "masculino"
masCont = 0
perceMascuResp_nao = 0

femenino = " femenino"
femenino_sim_r_sim = 0
qtdSexo_femenino = 0
sim = "sim"
qtdPessoas_sim = 0
qtdpessoas_nao = 0
cont = 0
nao = "nao"
for i in range(0,10):
    sexo[i] = str(input("digite( seu sexo --femenino- ou -masculino"+str([i + 1]) +""))
    resposta[i] = str(input(" digite se vocês gostaram do produto ( s - sim ou - n não"+ str([i + 1]) +""))
#o n ́umero de pessoas que responderam sim;
for i in resposta:
    if(i == sim):
        cont = cont + 1
print(cont)
#o n ́umero de pessoas que responderam n ̃ao;
for i in resposta:
    if(i == nao):
        qtdpessoas_nao = qtdpessoas_nao +  1
print(qtdpessoas_nao)
#o n ́umero de mulheres que responderam sim; e
for i in range(0,10):
    if(sexo[i] == femenino) and (resposta[i] == sim ):
        qtdSexo_femenino = qtdSexo_femenino + 1
qtdSexo_femenino = qtdSexo_femenino + 1
print(qtdSexo_femenino)
#a percentagem de homens que responderam n ̃ao, entre todos os homens analisados.
for i in range (0,10):
    if(sexo[i] == masculino) and (resposta[i] == nao ):
        masCont = masCont + 1
        perceMascuResp_nao = perceMascuResp_nao + 1
masCont = masCont + 1
perceMascuResp_nao = perceMascuResp_nao * masCont / masCont
print("a percentagem de homens que responderam n ̃ao, entre todos os homens analisados.".format(perceMascuResp_nao))













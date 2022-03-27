desejaVotar = "s"
escolha = 0
cont = cont3 = cont4 = cont5 = cont6 =  0
cont2 = 0
median = mediab = 0
print("--Escolha No Menu o Seu Candidato--")
print('DIGITE --1-- Para votar em Lula')
print('DIGITE --2-- Para votar em Bolsonaro')
print('DIGITE --3-- Para votar em Roberto')
print('DIGITE --4-- Para votar em Marina')
print('DIGITE --5-- Para votar nulo')
print('DIGITE --6-- Para em branco')


while desejaVotar in "Ss":

    escolha = int(input("Digite o numero do seu candidato"))
    desejaVotar = str(input("Digite (--F--) para para finalizar a sessão é (--S-)- para continuar ").upper().strip())
    if(escolha == 1):
        cont += 1

    if(escolha == 2):
        cont2 += 1

    if(escolha == 3):
        cont3 += 1

    if (escolha == 4):
        cont4 += 1
    if (escolha == 5):
        cont5 += 1
        median = median + escolha
    if (escolha == 6):
        cont6 += 1
        mediab = mediab + escolha







print("A quantidade de votos no candidato Lula é {}".format(cont))
print("A quantidade de votos no candidato Bolsonaro é {}".format(cont2))
print("A quantidade de votos no candidato Roberto é {}".format(cont3))
print("A quantidade de votos no candidato Marina é {}".format(cont4))
print("A quantidade de votos nulos é {} é a porcentagem de votos nulose é:{}".format(cont5,cont5 * median/100))
print("A quantidade de votos em branco é {} e a porcentagem de votos em branco é {}".format(cont6,cont6*mediab/100))








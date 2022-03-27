inicio = 1
cont = 0
contmais = recebemaior = 0
maior = menor = 0
while(inicio>0):
    num = int(input("Digite um numero"))
    inicio = int(input("digite 0 para finalizar é 1 para continuar"))
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if(num > maior):
            maior = num
        if(num< menor):
            menor = num
    if(num==0):
        print("você digitou numero negativo")




print(" o maior numero foi {} é o menor numero foi{}".format(maior,menor))

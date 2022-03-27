cont = 0
idade = 1
media = 0
while(idade > 0):
    idade = int(input("Digite sua idade"))
    if(idade >= 0):
        cont = cont + idade
        media = media + 1
print("a media das idade digitadas é ={}".format(cont/media))


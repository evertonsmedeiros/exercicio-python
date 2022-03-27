print("==========Escolha entre as opçoes:=========\n")
sair = "c"
cont = 0
media = 0
c = 0
mediap = 0
n1 = n2 = n3 = p1 = p2 = p3 = 0
while sair in 'Cc':
    esc = int(input(" 1 Media aritimetica.--2-- Media ponderada"))

    if(esc == 1):
        cont += 1
        n1 = float(input("digite a primeira nota"))
        n2 = float(input("digite a segunda nota"))
        sair = str(input("escolha --S-- para sair ou --C-- para continuar ").upper().strip()[0])

    media = (n1 + n2) / 2
    print(" A Media entre as duas notas é :{}".format(media))

    if(esc == 2):
        c += 1
        n1 = float(input("digite a primeira nota"))
        n2 = float(input("digite a segunda nota"))
        n3 = float(input("digite a terceira nota"))
        p1 = float(input("digite o peso 1: "))
        p2 = float(input("digite o peso 2:"))
        p3 = float(input("digite o peso :3"))
        sair = str(input("escolha --S-- para sair ou --C-- para continuar ").upper().strip()[0])

    mediap = (n1*p1+n2*p2+n3*p3)/10
    print("A media ponderada é {}".format(mediap))




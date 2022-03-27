#Uma loja utiliza o c ́odigo V para transa ̧c ̃ao `a vista e P para transa ̧c ̃ao a prazo.  Fa ̧ca
vista = 0
prazo = 0
total = 0
codigo = 0
valor = 0
i = 0
for i in (i,5 ):
    i = i + 1
    codigo = float(input("digite o codigo"))
    valor = float(input("digite o valor"))
    if(codigo == vista):
        vista  += valor
        prazo = valor + 2
    else:prazo += valor
    print("o valor das compras a vistas {} ".format(vista + valor))
    print("o valor das compras a prazo {} ".format(prazo + valor))
    print("o valor das compras a vistas {} mais prazo {} ".format(vista,prazo))
    print("o valor das compras a prazo {} ".format(  1* prazo/3))





#4.Fa ̧ca um programa que receba um n ́umero, calcule e mostre a tabuada desse n ́umero.Exemplo:
num = int(input("digite um numero para ver sua tabuada"))
for i in range(1,11):
    print("{} x {:2} = {}".format(num,i,num*i))
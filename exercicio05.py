#5.  Fa ̧ca um programa que mostre as tabuadas dos n ́umeros de 1 a 10.
n = int(input("digite um numero"))
for i in range(1, n):
    i += 1

    print("tabela  ")
    for num in range(10 ):
        num =  num+ 1


        print(i, 'x', num, '=', i * num)



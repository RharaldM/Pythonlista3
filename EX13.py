def funcao1(n):
    for c in range(1, n + 1):
        cont = 1
        while True:
            print(c, end=' ')
            if cont == c:
                break
            cont += 1
        print()


n = int(input('Digite um número: '))
funcao1(n)
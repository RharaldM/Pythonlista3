def funcao01(n: object) -> object:
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')

print('POSITIVO OU NEGATIVO')
n = int(input('digite um número: '))
print('Este número é', end=' ')
funcao01(n)
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os
# números.

inteiros = []
soma = 0
multiplicacao = 1
print('Digite 5 numeros inteiros a seguir')

for numero in range(5):
    n = inteiros.append(int(input()))

for x in inteiros:
    soma += x
    multiplicacao *= x

print('A soma desses numeros é', soma)
print('A multiplicação desses números é: ', multiplicacao)
print('Os números são', inteiros)





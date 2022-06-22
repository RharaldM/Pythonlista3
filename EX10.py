matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor para [{},{}]: ".format(l, c)))

k = int(input("Escolha um número para multiplicar os elementos: "))

for l in range(3):
    for c in range(3):
        matriz[l][c] = k * matriz[l][c]
print(matriz)


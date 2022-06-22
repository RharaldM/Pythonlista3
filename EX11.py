matrizA = [[0, 0], [0, 0]]
matrizB = [[0,0],[0,0]]
for a in range(2):
    for b in range(2):
        matrizA[a][b] = int(input("Digite os números para [{},{}]: ".format(a, b)))

for c in range(2):
    for d in range(2):
        matrizB[c][d] = int(input("Digite os números para [{},{}]: ".format(c, d)))

C = [[0,0], [0,0]]
C[0][0] = matrizA[0][0] + matrizB[0][0]
C[1][0] = matrizA[1][0] + matrizB[1][0]
C[0][1] = matrizA[0][1] + matrizB[0][1]
C[1][1] = matrizA[1][1] + matrizB[1][1]

print("A soma das matrizes A e B é {}".format(C))
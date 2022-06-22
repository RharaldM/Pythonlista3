#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
#cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
acimamedia = 0

for aluno in range(2):
    somanotas = 0

    str(input("digite o nome do {}° aluno: ".format(aluno+1)))

    for nota in range(4):
        somanotas += int(input("Digite a nota do aluno: "))

    notas.append(somanotas / 4)

    if notas[aluno] >= 7:
        acimamedia += 1

print('O número de alunos acima da média é de:',acimamedia)


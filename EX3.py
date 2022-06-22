idade = []
altura = []
cont_pessoa = 0

for x in range(1,3,1):
    idade.append(float(input('Digite a idade da {}° pessoa: '.format(cont_pessoa + x))))
    altura.append(float(input('Digite sua altura: ')))

idade.reverse()
print(idade)
altura.reverse()
print(altura)

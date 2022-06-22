vetor1 = []
vetor2 = []
vetor3 = []
contador_e = 0
for a in range(1,11):
    vetor1.append(input('Digite o {}° elemento do primeiro vetor: '.format(contador_e+a)))
print('='*50)
for b in range(1,11):
    vetor2.append(input(('Digite o {}° elemento do primeiro vetor: '.format(contador_e+b))))

for c in range(10):
    vetor3.append(vetor1[c])
    vetor3.append(vetor2[c])

print(vetor3)
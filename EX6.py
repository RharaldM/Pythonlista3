s1 = str(input('Digite uma frase qualquer: ')).strip()
s2 = str(input('Digite outra frase qualquer: ')).strip()

print('O tamanho de "{}" possue {} caracteres'.format(s1,len(s1)))
print('O tamanho de "{}" possue {} caracteres'.format(s2,len(s2)))

if len(s1) != len(s2):
    print("As duas strings possuem tamanhos diferentes")

else:
    print("As duas strings possuem tamanhos iguais")

if s1 != s2:
    print("As strings possuem contéudos diferentes")
else:
    print("As strings possuem conteúdos iguais")


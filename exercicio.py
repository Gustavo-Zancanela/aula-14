classe = {}
while True:
    nome = input ('Digite o nome do aluno: ')
    if nome == '':
        break
    nota = int(input('Digite a nota do aluno (0-10): '))
    if nota not in range(0,11):
        break
    if nota in classe:
        classe[nome] += (nota,)
    else:
        classe[nome] = (nota,)
    
for nome in sorted(classe.keys()):
    soma = 0
    contagem = 0
    for nota in classe[nome]:
        soma += nota
        contagem += 1
print(nome, ':', soma/contagem)
    
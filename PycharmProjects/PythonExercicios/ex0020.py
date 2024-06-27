import random
print('*'*50)
print(f'{'SORTEIO DE APRESENTAÇÃO':^50}')
print('*'*50)
a1 = input('\nDigite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
sorteio = [a1, a2, a3, a4]
random.shuffle(sorteio)
print(f'\nA ordem de apresentação dos alunos será: \n{sorteio}.\n')
print('*'*50)

import random
print('-'*60)
print(f'{'SORTEIO LIMPA QUADRO':^60}')
print('-'*60)
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
sorteio = random.choice([a1, a2, a3, a4])
print(f'\nO escolhido para limpar o quadro de hoje foi o(a) {sorteio}!\n')
print('-'*60)

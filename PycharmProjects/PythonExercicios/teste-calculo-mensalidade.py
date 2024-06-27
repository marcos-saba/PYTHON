print('-'*50)
print(f'{'\033[1;4mCALCULADORA DE MENSALIDADES\033[m':^60}')
print('-'*50)
mensalidade = float(input('\nMensalidade inicial(R$): '))
taxa = float(input('Taxa de aumento por semestre(%): '))
total_semestre = int(input('Total de semestres: '))
semestre = mensalidade * 6
total = semestre
print(f'\nMensalidade \033[1;34m1º\033[m semestre: \033[1;33mR${mensalidade:.2f}\033[m')
print(f'Total \033[1;34m1º\033[m semestre: \033[1;33mR${semestre:.2f}\033[m')
print(f'Total acumulado até \033[1;34m1º\033[m semestre: \033[1;33mR${semestre:.2f}\n\033[m')
for c in range(1, total_semestre):
    aumento = mensalidade + (mensalidade * taxa / 100)
    mensalidade = aumento
    semestre = mensalidade * 6
    total += semestre
    s = c + 1
    print(f'Mensalidade \033[1;34m{s}º\033[m semestre: \033[1;33mR${mensalidade:.2f}\033[m')
    print(f'Total \033[1;34m{s}º\033[m semestre: \033[1;33mR${semestre:.2f}\033[m')
    print(f'Total acumulado até \033[1;34m{s}º\033[m semestre: \033[1;33mR${total:.2f}\n\033[m')
print('_'*50)
input(f'{'Pressione Enter para sair...':^50}')

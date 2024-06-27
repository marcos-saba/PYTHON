mensalidade = float(input('Mensalidade inicial(R$): '))
taxa = float(input('Taxa de aumento por semestre(%): '))
total_semestre = int(input('Total de semestres: '))
semestre = mensalidade * 6
total = semestre
print(f'\nMensalidade 1º semestre: R${mensalidade:.2f}')
print(f'Total 1º semestre: R${semestre:.2f}')
print(f'Total acumulado até 1º semestre: R${semestre:.2f}\n')
for c in range(1, total_semestre):
    aumento = mensalidade + (mensalidade * taxa / 100)
    mensalidade = aumento
    semestre = mensalidade * 6
    total += semestre
    s = c + 1
    print(f'Mensalidade {s}º semestre: R${mensalidade:.2f}')
    print(f'Total {s}º semestre: R${semestre:.2f}')
    print(f'Total acumulado até {s}º semestre: R${total:.2f}\n')


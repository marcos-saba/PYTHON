print(f'{' CALCULADORA DE SALÁRIO ':=^75}')
sal = float(input('\nDigite o valor do salário(R$): '))
if sal > 1250:
    novo = sal + (sal*10/100)
else:
    novo = sal + (sal*15/100)
print(f'O salário atual é de R${sal:.2f} e com o novo aumento será de R${novo:.2f}.\n')
print(f'{' FIM ':=^75}')

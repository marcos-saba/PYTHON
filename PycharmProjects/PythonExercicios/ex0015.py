print('='*10, 'ALUGUEL DE CARROS', '='*10)
dia = int(input('Informe a quantidade de dias: '))
km = float(input('Informe os quilômetros rodados(km): '))
valor = dia * 60 + km * 0.15
print(f'O valor total do aluguel do carro por {dia} dias e {km}km rodados é de R${valor:.2f}.')

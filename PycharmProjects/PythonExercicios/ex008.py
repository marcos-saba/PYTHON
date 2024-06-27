print('='*5, 'CONVERSÃO DE MEDIDAS', '='*5)
m = float(input('Digite um valor (metro): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'Valor em quilômetros: {km}km \nValor em hectômetro: {hm}hm '
      f'\nValor em decâmetro: {dam}dam')
print(f'Valor em decímetro: {dm:.0f}dm \nValor em centímetro: {cm:.0f}cm '
      f'\nValor em milímetro: {mm:.0f}mm')

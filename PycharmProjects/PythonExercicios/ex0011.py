print('*'*15, 'CÁLCULO DE TINTA', '*'*15)
l = float(input('Informe a largura da parede (m): '))
a = float(input('Informe a altura da parede (m): '))
area = l * a
tinta = area / 2
print(f'\nAltura da parede (m): {l}'
      f'\nLargura da parede (m): {a}'
      f'\nÁrea da parede (m²): {area:.2f}'
      f'\nQuantidade de tinta necessária (l): {tinta:.2f}\n')
print('*'*20, 'FIM', '*'*20)

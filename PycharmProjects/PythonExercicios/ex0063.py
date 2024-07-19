print(f'{' SEQUÊNCIA DE FIBONACCI ':=^60}')
n = int(input('\nDigite o número de elementos da sequência de Fibonacci: '))
a = 0
b = 1
cont = 1
if n < 2:
   print(f'\nO primeiro elemento da Sequência de Fibonacci é:')
   print('-'*60)
   print(0)
   print('-'*60)
elif n == 2:
   print(f'\nOs {n} primeiros elementos da Sequência de Fibonacci são: ')
   print('-'*60)
   print(f'{a}->{b}')
   print('-'*60)
else:
   print(f'Os {n} primeiros elementos da Sequência de Fibonacci são: ')
   print('-'*60)
   print(f'{a}->{b}', end='->')
   while cont < n-1:
      f = a + b
      if a > 1:
         b = a
      a = f
      #a = b
      #b = f
      if cont == n-2:
         print(f, end='')
      else:
         print(f, end='->')
      cont +=1
   print('')
   print('-'*60)
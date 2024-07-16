print(f'{' TABUADA TURBINADA ':=^50}')
num = int(input('Digite um número para mostra a sua tabuada: '))
print('-'*50)
for c in range(1, 11):
    print(f'{num:>20} x {c:>2} = {num * c:^2}')
print('-'*50)

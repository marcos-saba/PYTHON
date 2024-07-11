print(f'{' TABUADA TURBINADA ':=^50}')
num = int(input('Digite um número para mostra a sua tabuada: '))
m = 0
print('-'*50)
for c in range(1, 11):
    m = num * c
    print(f'{num:>20} x {c:^2} = {m:^2}')
print('-'*50)


num = int(input('Digite um número: '))
digito = str(num + 10000)
'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
'''
print(f'O número digitado foi: {num}')
print(f'Unidade: {digito[-1]}')
print(f'Dezena: {digito[-2]}')
print(f'Centena: {digito[-3]}')
print(f'Milhar: {digito[-4]}')

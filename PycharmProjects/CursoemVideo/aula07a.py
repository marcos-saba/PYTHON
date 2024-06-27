print('='*10, 'TESTE DE CÁLCULO', '='*10)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
t = 'teste'
print('A soma é {}, o produto é {} e a divisão é {:.2f}.'.format(s, m, d), end=' ') # não quebrar linha: end=' ';
print('A divisão inteira é {} \ne a potência é {}.'.format(di, e)) # quebrar linha: \n






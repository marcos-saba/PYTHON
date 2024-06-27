n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}.')
if m >= 6.0:
    print('Você passou! Parabéns seu nerd!!')
else:
    print('Se fu! Estude mais na próxima!')
# condição simplificada: print('PARABENS!' if m>=6.0 else 'ESTUDE MAIS!')
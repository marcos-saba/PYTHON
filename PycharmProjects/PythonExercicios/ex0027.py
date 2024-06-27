nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'O seu nome completo é {nome}.')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')  #n[len(n)-1]

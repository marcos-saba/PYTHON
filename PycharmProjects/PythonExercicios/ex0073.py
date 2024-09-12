times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Internacional',
         'Atlético-MG', 'Brangantino', 'Athletico_PR', 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians',
         'Vitória', 'Cuiabá', 'Atlético-GO')
print('Lista de times do Brasileirão:\n')
for time in times:
    print(time)
print('='*30)
print('\nOs 5 primeiros são:\n ')
for time in times[0:5]:
    print(time)
print('='*30)
print('\nOs 4 últimos são: \n')
for time in times[14:19]:
    print(time)
print('='*30)
print('\nTimes em ordem alfabética: \n')
for time in sorted(times):
    print(time)
print('='*30)
print(f'\nO Internacional está na {times.index('Internacional') + 1}ª posição.')

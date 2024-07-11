from time import sleep
import emoji

print('*' * 30)
print(f'{'FOGOS':^30}')
print('*' * 30)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('')
for c in range(0, 3):
    print('BOM!', emoji.emojize(':fireworks:'), end=' ')
    sleep(0.3)
print(f'\n\n{' FIM ':*^30}')

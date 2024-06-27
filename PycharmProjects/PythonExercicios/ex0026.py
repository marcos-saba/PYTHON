frase = str(input('Digite uma frase: ').strip())
print(f'A letra "A" aparece na frase {frase.upper().count('A')} vezes.')
print(f'A letra "A" aparece pela primeira vez na frase na posição {frase.upper().find('A')+1} '
      f'\ne pela última vez na posição {frase.upper().rfind('A')+1}.')

cidade = str(input('Digite o nome de uma cidade: ')).strip()
cid = cidade.upper().split()  #(cidade[:5].upper() == 'SANTO')
cid = str(cid[0].find('SANTO'))
print(f'A cidade {cidade.upper()} começa com a palavra "SANTO"? \n{cid.isnumeric()}')
n1 = float(input('Primeiro Número: : '))
n2 = float(input('Segundo Número: '))
n3 = float(input('Terceiro Número: '))

if n1 > n2 and n3:
    print('Maior: {}'.format(n1))

if n2 > n1 and n3:
    print('Maior: {}'.format(n2))

if n3 > n2 and n1:
    print('Maior: {}'.format(n3))

if n3 == n2 == n1:
    print('NÃO HÁ MAIOR')










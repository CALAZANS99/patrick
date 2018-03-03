n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

med = (n1 + n2)/2

if med > 0 and med < 4:
    print('SUA MÉDIA É DE {}'.format(med))
    print('CONCEITO E')
    print('REPROVADO')

if med >= 4 and med < 6:
    print('SUA MÉDIA É DE {}'.format(med))
    print('CONCEITO D')
    print('REPROVADO')

if med >= 6 and med < 7.5:
    print('SUA MÉDIA É DE {}'.format(med))
    print('CONCEITO C')
    print('APROVADO')

if med >= 7.5 and med < 9:
    print('SUA MÉDIA É DE {}'.format(med))
    print('CONCEITO B')
    print('APROVADO')

if med >= 9 and med <= 10:
    print('SUA MÉDIA É DE {}'.format(med))
    print('CONCEITO A')
    print('APROVADO')



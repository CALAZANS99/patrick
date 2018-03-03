p1 = float(input('preço produto 1: '))
p2 = float(input('preço produto 2: '))
p3 = float(input('preço produto 3: '))

if (p1 < p2) and (p1<p3):
    print('Compre o produto 1')

if (p2<p1) and (p2<p3):
    print('Compre o produto 2')

if (p3<p2) and (p3<p1):
    print('Compre o produto 3')

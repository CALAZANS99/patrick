l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 == l2 == l3:
    print('TRIÂNGULO EQUILÁTERO')

if l1 == l2 and l1 != l3:
    print('ISÓSCELES')

if l1 != l2 != l3:
    print('TRIÂNGULO ESCALENO')


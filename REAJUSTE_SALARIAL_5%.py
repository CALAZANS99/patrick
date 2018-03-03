s = float(input('Digite o salário: '))

if s <= 280:
    print('Salário antes do reajuste: {}'.format(s))
    print('Valor do aumento: {:.2f}'.format(s*1.2 - s))
    print('Novo salário: {}'.format(s*1.2))
    print('Percentual de aumento foi de 20%')

if s > 280 and s < 700:
    print('Salário antes do reajuste: {}'.format(s))
    print('Valor do aumento: {:.2f}'.format(s*1.15 - s))
    print('Novo salário: {}'.format(s*1.15))
    print('Percentual de aumento foi de 15%')

if s > 700 and s <1500:
    print('Salário antes do reajuste {}'.format(s))
    print('Valor do aumento {}'.format(s*1.1 - s))
    print('Novo salário: {}'.format(s*1.1))
    print('Percentual de aumento foi de 10%')

if s > 1500:
    print('Salário antes do reajuste {}'.format(s))
    print('Valor do aumento {}'.format(s*1.05 - s))
    print('Novo salário {}'.format(s*1.05))
    print('Percentual de aumento doi de 5%')







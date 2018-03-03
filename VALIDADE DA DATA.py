dd = int(input('Digite o dia: '))
mm = int(input('Digite o mês: '))
aaaa = int(input('Digite o ano: '))


if dd > 1 and dd <= 31 and mm >= 1 and mm < 13 and aaaa >= 1:
    print('A DATA {}/{}/{} É VÁLIDA'.format(dd, mm, aaaa))

else:
    print('A DATA {}/{}/{} É INVÁLIDA'.format(dd, mm, aaaa))





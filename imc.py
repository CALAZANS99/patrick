print('\033[1;31m===== CALCULE SEU ÍNDICE DE MASSA CORPORAL =====\033[m')
print(' ')
h = float(input('\033[1;34mSua altura: '))
m = int(input('\033[1;34mSua massa: '))

imc = m/h**2

print('Seu IMC é: {:.1f}'.format(imc))
print(' ')

print('\033[4;30m===== VEJA, COM BASE NO RESULTADO, SEU ESTADO DE SAÚDE. =====')

print(' ')

if imc <= 18.5:
     print('\033[1;33mVOCÊ ESTÁ ABAIXO DO SEU PESO IDEAL')

if imc >=18.6 and imc <24.6:
    print('\033[1;32mPARABÉNS! VOCÊ ESTÁ EM SEU PESO IDEAL.')

if  imc > 25 and imc <= 29.9:
    print('\033[1;33mVOCÊ ESTÁ COM LEVE SOBREPESO.')

if imc > 30 and imc <=34.9:
    print('\033[1;31mOBESIDADE GRAU 1')

if imc >= 35 and imc <=39.9:
    print('\033[1;31mOBESIDADE GRAU 2')

if imc > 40:
    print('\033[1;31mOBESIDADE GRAU 3')




